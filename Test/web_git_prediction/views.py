'''api module'''
import subprocess
import urllib
import os

import flask
import logging

import requests
from flask import json, Flask
import json
from flask import request as rq
from flask import Response
from fetching_data.test_data import TestData
from web_git_prediction.app import app
from fetching_file_data.fetching_file_data import Fetch_file
from fetching_file_data.test_data import TestData1
from fetching_data.fetching_data import Fetch
from search.search import Search
from comments.comment import Comment

from store_model.store_model import StoreModel
import fetching_file_data.helper
from fetching_data import commit_api
from web_git_prediction import file_predict_comment
from web_git_prediction.linter import lint
from web_git_prediction.logic_error import logic
from utils.utils import Utils

log = logging.getLogger(__name__)
config = Utils().get_config_file('config.ini')
user_id = config.get('GithubCredential', 'user_id', raw=True)
password = config.get('GithubCredential', 'password')


@app.route('/', methods=['GET', 'POST', 'HEAD'])
def index():
    """Index page"""
    return 'Welcome'


@app.route('/github/', methods=['GET', 'POST', 'HEAD'])
def api_github_message():
    """api for sending comments"""
    if rq.headers['Content-Type'] == 'application/json':
        my_info = json.dumps(rq.json)
        payload = json.loads(my_info)
        if not payload['action'] == 'closed':
            comment_url_new = payload['pull_request']['comments_url']
            model = StoreModel().loadData()
            tdf = TestData()
            tdf1 = TestData1()
            parameter_dict = tdf.fetcher(my_info)
            extension_file = tdf1.file_fetcher(my_info)
            feature_dict = parameter_dict['feature_dict']
            comment_url = parameter_dict['comment_url']
            comment_body_pred = tdf.test_feeder(feature_dict, model)
            if comment_body_pred == 1:
                comment_file = file_predict_comment().predict_file_criticality(payload)
                if comment_file == 1:
                    linter_returned = lint(payload)

                    if linter_returned == 1:
                        logic_returned = logic(payload)
                        if logic_returned == 2:
                            comment_body = 'GIT ASSIST PREDICTION : All Checks Passed. Ready For Further Review.'
                            Comment.post_comment(comment_url, comment_body)
                            return "Logic pass"
                        else:
                            print("In Views and logic part")
                            comment_body = logic_returned
                            print("Comment:", comment_body)
                            headers = {'Content-Type': 'application/json'}
                            myurl = '%s' % comment_url
                            post_comment_data = '{\"body\":\"%s\"}' % comment_body
                            post_comment_json = json.loads(post_comment_data, strict=False)
                            response = requests.post(myurl, auth=(user_id, password), headers=headers,
                                                     json=post_comment_json)
                            if response.status_code == 201:
                                print("Successfully posted a comment")
                            else:
                                print("Failed to post a response with http status code : ", response.status_code)
                            return "logical error"
                    else:
                        comment_body = linter_returned
                        myurl = '%s' % comment_url
                        Comment.post_comment(myurl, comment_body)
                        return "linting error"


                else:
                    headers = {'Content-Type': 'application/json'}
                    myurl = '%s' % comment_url
                    post_comment_data = '{\"body\":\"%s\"}' % comment_file
                    post_comment_json = json.loads(post_comment_data, strict=False)
                    response = requests.post(myurl, auth=(user_id, password), headers=headers,
                                             json=post_comment_json)
                    if response.status_code == 201:
                        print("Successfully posted this comment")
                    else:
                        print("Failed to post a response with http status code : ", response.status_code)
                    return "Critical found"

            else:
                comment_body = 'GIT ASSIST PREDICTION : Probability of being Rejected'
                Comment.post_comment(comment_url, comment_body)
                return "Pull level error"

        else:
            print ("Closed pull request")
            return "closed PR"

"""         
        prediction_response = json.dumps({"state": "closed pull request"})
        app.logger.info("closed pull request")
        res = Response(prediction_response, status=200, mimetype='application.json')
        return res"""


@app.route('/api/connection/', methods=['GET', 'POST', 'HEAD'])
def api_getconnection():
    """api for creating connection"""
    if rq.method == 'POST':
        user_id = rq.form['user_id']
        password = rq.form['password']
        search_keyword = rq.form['search_keyword']
        response = requests.get('https://api.github.com', auth=(user_id, password))
        status = response.headers['Status']
        if status == '401 Unauthorized' or status == 'Forbidden':
            app.logger.info('failed to log in.... Please try again')
            msg = json.dumps({"status": 401, "authorization": "False"})
            res = Response(msg, status=201, mimetype='application.json')
            return res
        else:
            owner_repositories = Search.search(search_keyword)
            owner_repositories_dict = {}
            owner_repositories_dict = owner_repositories
            connection_response = json.dumps({"status": 200, "authorization": "True",
                                              "owner_repositories_list": owner_repositories_dict})
            app.logger.info('logged in successfully')
            res = Response(connection_response, status=201, mimetype='application.json')
            return res


@app.route('/api/pulls_extract/', methods=['POST', 'GET'])
def result():
    """api for pull level features"""
    if rq.method == 'POST':
        search_keyword = rq.form['search_keyword']
        FETCH_OBJ = Fetch()
        owner_repositories = Search.search(search_keyword)
        for i in owner_repositories:
            owner_name = i["owner_name"]
            repository_name = i["repository_name"]
            FETCH_OBJ.json_to_csv_conversion(owner_name, repository_name)
        msg = json.dumps({"status": 200, "state": "pulls level Csv is being Constructed"})
        res = Response(msg, status=201, mimetype='application/json')
        return res


@app.route('/api/files_extract/', methods=['POST', 'GET'])
def fileresult():
    """api for file level features"""
    if rq.method == 'POST':
        search_keyword = rq.form['search_keyword']
        FETCH_OBJ = Fetch_file()
        owner_repositories = Search.search(search_keyword)
        for i in owner_repositories:
            owner_name = i["owner_name"]
            repository_name = i["repository_name"]
            FETCH_OBJ.json_to_csv(owner_name, repository_name)
        msg = json.dumps({"status": 200, "state": "files level Csv is being Constructed"})
        res = Response(msg, status=201, mimetype='application/json')
        return res
