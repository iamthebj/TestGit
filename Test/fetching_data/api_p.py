import json
from flask import json
from flask import request
from flask import Flask, Response
from commit_api import *
from comments.comment import Comment
from test_data import TestData
from fetching_file_data.test_data import *
from store_model.store_model import StoreModel
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)


@app.route('/')
def index():
    """Index page"""
    return 'Welcome'


@app.route('/github/', methods=['GET', 'POST', 'HEAD'])
def api_github_message():
    """api for sending comments"""
    if request.headers['Content-Type'] == 'application/json':
        print('inside server ')
        my_info = json.dumps(request.json)
        payload = json.loads(my_info)
        if not payload['action'] == 'closed':
            model = StoreModel().loadData()
            tdf = TestData()
            tdf1 = TestData1()
            parameter_dict = tdf.fetcher(my_info)
            extension_file = tdf1.file_fetcher(my_info)
            feature_dict = parameter_dict['feature_dict']
            comment_url = parameter_dict['comment_url']
            comment_body = tdf.test_feeder(feature_dict, model)
            file_comment_body = tdf1.file_test_feeder(extension_file[0], extension_file[1])
            Comment.post_comment(comment_url, comment_body)
            Comment.post_comment(comment_url, str(file_comment_body))
            app.logger.info(comment_body)
            prediction_response = json.dumps({"state": comment_body})
            app.logger.info(comment_body)
            res = Response(prediction_response, status=200, mimetype='application.json')
            return res
        prediction_response = json.dumps({"state": "closed pull request"})
        app.logger.info("closed pull request")
        res = Response(prediction_response, status=200, mimetype='application.json')
        return res


@app.route("/commit_api_call/", methods=['GET', 'POST'])
def commit_api_result():
    apicall_obj = api_call()
    apicall_obj.postman()
    return json.dumps(apicall_obj.critical_files())


if __name__ == '__main__':
    app.run(host="10.44.205.121", port=8000, debug=True)
    #app.run()
