import os
import subprocess
import urllib

import requests


def lint(payload):
    global syntax_check, process, comment_body
    url = payload['pull_request']['url']
    url = url + '/files'
    r = requests.get(url)
    a = r.json()
    # print(a)
    print("Received Pull Request for %d Changed Files" % (len(a)))
    print("Initializing Linting Process")
    i = 0
    global syntax_error
    syntax_error = []
    filelist = []
    comment_body = ""
    for i in range(len(a)):
        raw = (a[i]['raw_url'])
        #print(raw)
        filename = (a[i]['filename']).split("/")
        file = filename[-1]

        re = urllib.request.urlopen('%s' % raw)
        # returned_value = os.system("start \"\" %s" %raw)
        data = re.read()
        dst = open("%s" % file, "wb")
        dst.write(data)
        dst = open("%s" % file, "r")
        print("Checking syntax errors for File: %d. %s" % (i + 1, file))

        file_ext = (file).split(".")
        print("File extension of the file: %s" % file_ext[-1])
        # HARD CODES FOR LINTERS
        lint = None
        # PHP
        if file_ext[-1] == 'php':
            lint = 'D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/php/php.exe -l'
        # PY
        elif file_ext[-1] == 'py':
            lintpy = 'pycodestyle.py --ignore=E115,E116,E113,E901,E265,W291,W293,E226,W226'
            env_path = 'D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/py'
            cmd = '%s %s' % (lintpy, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       env=dict(os.environ, PATH=env_path)).communicate(0)
            # print(process)
            syntax_check = ""
            for j in range(len(process)):
                syntax_check = syntax_check + process[j].decode("utf_8")
                print(syntax_check)
                if "No syntax errors detected" in syntax_check:
                    syntax_check = ""
        # C
        elif file_ext[-1] == 'c':
            env_path = 'D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/c_cpp/bin'
            lintgcc = 'gcc'
            print("Cloned file: %s deleted" % file)
            print("Linting file : %s" % file)
            cmd = '%s %s' % (lintgcc, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       env=dict(os.environ, PATH=env_path)).communicate(0)
            #syntax_check = str(process).split(", b'")[-1]
            syntax_check = ""
            for j in range(len(process)):
                syntax_check = syntax_check + process[j].decode("utf_8")
                print(syntax_check)
        # CPP
        elif file_ext[-1] == 'cpp':
            env_path = 'D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/c_cpp/bin'
            lintgpp = 'g++'
            print("Cloned file: %s deleted" % file)
            print("Linting file : %s" % file)
            cmd = '%s %s' % (lintgpp, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       env=dict(os.environ, PATH=env_path)).communicate(0)
            #print(process)
            #syntax_check = str(process).split(", b'")[-1]
            syntax_check = ""
            for j in range(len(process)):
                syntax_check = syntax_check + process[j].decode("utf_8")
                print(syntax_check)

        # JAVA (UNDER TEST)
        elif file_ext[-1] == 'java':
            env_path = 'C:/Program Files/Java/jdk-9.0.4/bin'
            lintjava = 'java -jar D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/java/checkstyle-5.8-all.jar -c D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/java/google_checks.xml'
            cmd = '%s %s' % (lintjava, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE,
                                               env=dict(os.environ, PATH=env_path)).communicate(0)
            syntax_check = ""
            for j in range(len(process)):
                syntax_check = syntax_check + process[j].decode("utf_8")
            print(syntax_check)

        # JAVASCRIPT (UNDER TEST)
        elif file_ext[-1] == 'js':
            env_path = 'D:/biswajit/GIT_PREDICTION_LATEST_With_Logical/git_prediction/Linters/js'
            lintjs = 'gjslint'
            print("Cloned file: %s deleted" % file)
            print("Linting file : %s" % file)
            cmd = '%s %s' % (lintjs, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       env=dict(os.environ, PATH=env_path)
                                       ).communicate(0)
            syntax_check = ""
            for i in range(len(process)):
                syntax_check = syntax_check + process[i].decode("utf_8")
                syntax_check = syntax_check.replace(":", "-")
            syntax_check = syntax_check.split('')
            syntax_check = syntax_check[0]
            print(syntax_check)

        else:
            print("No linter found for %s extension" % file_ext[-1])
            s = "No linter found for %s extension" % file_ext[-1]
            syntax_check = ""

        if (lint != None):
            # print("Cloned file: %s deleted" % file)
            print("Linting file : %s" % file)
            cmd = '%s %s' % (lint, file)
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE).communicate(0)
            syntax_check = ""
            for j in range(len(process)):
                syntax_check = syntax_check + process[j].decode("utf_8")
                #print (syntax_check)
                if "No syntax errors detected" in syntax_check:
                    syntax_check = ""

        # p = str(p)
        # p = p[2:-1]
        #a = process[-1]
        # if a == b'':
        # q = "No syntax error found"
        # print(q)
        #a = process[-1]
        if syntax_check != "":
            filelist.append(file)
            #print("Syntax error found: %s" % syntax_check)
            #q = "Syntax error(s) found:"
        dst.close()
        os.remove("%s" % file)
        #s = "%s %s" % (q, syntax_check)
        syntax_error.append(syntax_check)
        i = i + 1

    if filelist:
        filelist = list(dict.fromkeys(filelist))
        filelist = ', '.join(filelist)
        syntax_error = ', '.join(map(str, syntax_error))
        comment_body = "Syntax Error(s) found: <br> %s" %syntax_error
        syntax_error = []
        return comment_body
    else:
        comment_body = "No syntax error found in any file."
        syntax_error = []
        #return comment_body
        return 1
