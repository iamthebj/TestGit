import requests
from urllib import request
import lizard
from utils.utils import Utils
import os
temp1 = ""
merge_file = []
branches_criticality={}
branches=[]
commit_file_data = []
counter = 0
changed_lines = 0
#file_dict_critical = {}
file_dict1_non_critical = {}
config = Utils().get_config_file('config.ini')
user_id = config.get('GithubCredential', 'user_id', raw=True)
password = config.get('GithubCredential', 'password')
requests_commit = config.get('commit_api', 'commit_url')
requests_merged = config.get('merge_api', 'merge_url')
branches_repo = config.get('commit_api', 'branches_repo')
branches_repos = requests.get(branches_repo, auth=(user_id, password)).json()
res_commit_api = requests.get(requests_commit, auth=(user_id, password)).json()
res_merge_files = requests.get(requests_merged, auth=(user_id, password))
temp_dir_complexity = config.get('temp_directory', 'temp_dir')
class commit:

    def branches(self):
        for j in branches_repos:
            branches.append(j['name'])
        branches.remove("master")
        branches.remove("rish")
        branches.remove("rish1")

    def commit_files(self, file_name1, x, filename=None):
        commit_file_data = []
        temp = requests_commit + x
        self.res_commit_api1 = requests.get(temp, auth=(user_id, password)).json()
        for j in self.res_commit_api1['files']:
            if j['filename'] == file_name1:
                raw_url = ((j['raw_url']))
                response = request.urlopen(raw_url)
                data_file = (response.read())
                data_file = data_file.decode()
                commit_file_data.append(data_file)
                self.lines_data = commit_file_data[0].rsplit('\n')

    def lizard(self, file_name1):
        print(file_name1)
        for j in self.res_commit_api1['files']:
            if j['filename'] == file_name1:
                x = ((j['raw_url']))
                filename, file_extension = os.path.splitext(x)
                # print(filename +' '+ file_extension)
                response = request.urlopen(x)
                html = response.read()
                html = html.decode()
                full_path = temp_dir_complexity + file_extension
                with open(full_path, 'w') as f:
                    print(html, file=f)
                i = lizard.analyze_file(full_path)
                print(i.__dict__)
        try:
            temp1 = i.function_list[0].__dict__
            os.remove(full_path)
        except:
            print('Code not generic so no complexity')
            pass

    def repo_files(self, file_name1):
        res2 = requests.get(requests_merged + "/" + file_name1, auth=(user_id, password))
        for j in res2:
            merge_file.append(j.decode())
        self.merge_file_lines = merge_file[0].rsplit('\n')

    file_dict_critical = {}
    def cmp_file(self, file):
        complex_key = "cyclomatic_complexity"
        nonchanged_lines = 0
        if len(self.lines_data) < len(self.merge_file_lines):
            i = len(self.lines_data)
        else:
            i = len(self.merge_file_lines)
        for j in self.lines_data:
            for i in self.merge_file_lines:
                if j == i:
                    if j == '' or i == '':
                        pass
                    else:
                        nonchanged_lines += 1
                else:
                    pass
        perc_change_files = ((len(self.lines_data) - nonchanged_lines)/(len(self.merge_file_lines) - nonchanged_lines))*100
        del self.lines_data[:]
        if perc_change_files > 50:
            ret_val = []
            ret_val.append("critical")
            #complexity = complex_key + " : " + str(temp1[complex_key])
            ret_val.append(temp1)
            class_obj.file_dict_critical[file] = ret_val
        else:
            ret_val1 = []
            ret_val1.append("Not-Critical")
            ret_val1.append(temp1)
            class_obj.file_dict_critical[file] = ret_val1

    def branche(self,x):
        branches_criticality[x]=class_obj.file_dict_critical
        return (branches_criticality)

class api_call(commit):
    file_names = []
    count = 0
    def postman(self,class_obj):
        for x in branches:
            temp = requests_commit+x
            print(temp)
            res_commit_api1 = requests.get(temp,auth=(user_id, password)).json()
            for j in res_commit_api1['files']:
                self.file_names.append(j['filename'])
            for j in self.file_names:
                    class_obj.commit_files(j, x)
                    self.count += 1
                    class_obj.repo_files(j)
                    class_obj.lizard(j)
                    class_obj.cmp_file(j)
            abc=class_obj.branche(x)
            class_obj.file_dict_critical = {}
            print ("hello ttttt",class_obj.file_dict_critical)
        print (abc)

if __name__ == "__main__":
    class_obj = commit()
    apicall_obj = api_call()
    apicall_obj.branches()
    apicall_obj.postman(class_obj)
