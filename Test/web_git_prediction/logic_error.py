import os
import urllib


def logic(payload):
    file_count = 0
    file_ch_list = []
    file_list = []
    file_l = []
    filelist = []
    strg = ''
    Logical_error = ''
    i = 0
    flag=0
    logical_error_list = []
    diff_url = payload['pull_request']['diff_url']
    re = urllib.request.urlopen('%s' % diff_url)
    data = re.read()
    dst = open("file.txt", "wb")
    dst.write(data)
    dst = open("file.txt", "r")
    Lg_er = ""
    with open('file.txt') as myfile1:
        for line in myfile1.readlines():
            if "diff" in line:
                file_count = file_count + 1
                file_list = line.split('/')
                file_l.append(file_list[-1])
    # print(file_l)
    print("number of files changed:", file_count)
    with open('file.txt') as myfile1:
        for line in myfile1.readlines():
            strg = line + strg
            # print(strg)

    # print(strg)
    list_ch = strg.split("diff")
    # print(list_ch[3])
    # print(list_ch)
    for i in range(file_count + 1):
        f = open("%d.txt" % i, "w+")
        f.write(list_ch[i])
    for i in range(file_count):
        # print('In ',file_l[c-i-1])
        with open('%d.txt' % i) as myfile:
            Logical_error = ''
            for line in myfile.readlines():

                if "+" in line:
                    if "while True" in line:
                        flag=1
                        #print('Infinite loop: Check for break')
                        Logical_error = Logical_error + 'Infinite loop: Check for break\n'
                    if 'while(1)' in line:
                        flag=1
                        Logical_error = Logical_error + 'Infinite loop: Check for break\n'
                    if '/0' in line:
                        flag=1
                        Logical_error = Logical_error + 'Divide by Zero error\n'
                    if 'malloc' in line:
                        flag=1
                        Logical_error = Logical_error + 'Dyanamic memory allocation: Check for free function\n'
                    if 'calloc' in line:
                        flag=1
                        Logical_error = Logical_error + 'Dyanamic memory allocation: Check for free function\n'
                    if 'realloc' in line:
                        flag=1
                        Logical_error = Logical_error + 'Dyanamic memory allocation: Check for free function\n'
                    if 'for(' in line:
                        string = ''
                        list0 = line.split(' ')
                        for x in list0:
                            string += x

                        # print(string)
                        list1 = string.split('(')

                        list2 = list1[-1].split(';')

                        counter = (list2[0][0])
                        check_counter = (list2[1][0:2])

                        greater_c = '>' + counter
                        less_c = counter + '<'
                        greater_cc = '<' + counter
                        less_cc = counter + '>'
                        if check_counter == greater_c:
                            if '-' in list2[2]:
                                flag=1
                                Logical_error = Logical_error + "Infinte loop: Decrementing counter with wrong condition\n"

                        if check_counter == less_c:
                            if '-' in list2[2]:
                                flag=1
                                Logical_error = Logical_error + "Infinte loop: Decrementing counter with wrong condition\n"

                        if check_counter == greater_cc:
                            if '+' in list2[2]:
                                flag=1
                                Logical_error = Logical_error + "Infinte loop: Incrementing counter with wrong condition\n"
                        if check_counter == less_cc:
                            if '+' in list2[2]:
                                flag=1
                                Logical_error = Logical_error + "Infinte loop: Incrementing counter with wrong condition\n"

        if(flag==1):
            #logical_error_list.append(file_l[i])
            logical_error_list.append('In %s' % file_l[i] + Logical_error)
        myfile.close()
        os.remove("%d.txt" % i)
    dst.close()
    os.remove("file.txt")

    for j in logical_error_list:
        Lg_er = j + Lg_er
    #print(Lg_er)
    #print(Lg_er)
    #return(Lg_er)
    print(Lg_er)
    if(Lg_er):
        comment_body = Lg_er
        #print(comment_body)
        return comment_body
    elif(Lg_er == ''):
        return 2
