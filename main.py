
import os

option= int (input("""welcome in the freelance system
please
 enter 1 : if you are client
 enter 2 : if you are freelancer
"""))
if (option== 1):
    qu=input("you have an account ?! yes or no ")
    if (qu == "no"):
        username = input("enter the username\n")
        pwd = input("enter the password\n")
        id = input("enter the ID\n")
        email = input("enter the email\n")
        maindir = r'D:\pythonProject1\the system\client'
        foldernae = username
        filename = username + ".txt"
        folderpath = os.path.join(maindir, foldernae)
        fullpath = os.path.join(maindir, foldernae, filename)
        if os.path.exists(folderpath) == False:
            os.mkdir(folderpath)
            f = open(fullpath, "w")
            f.write(username)
            f.write(" ")
            f.write(pwd)
            f.write(" ")
            f.write(id)
            f.write(" ")
            f.write(email)
            f.write("\n")
            f.close()
        else:
            print("this username are exist ")
            exit()

    elif (qu=="yes") :
        username=input("enter the usernam : \n")
        id = input("enter the ID : \n")
        passward=input("enter the passward : \n")
        maindir = r'D:\pythonProject1\the system\client'
        foldernae = username
        filename = username + ".txt"
        folderpath = os.path.join(maindir, foldernae)
        fullpath = os.path.join(maindir, foldernae, filename)
        for lines in open(fullpath,"r").readlines():
            log_info = lines.strip().split(" ")
            if (username ==log_info[0]) and (passward == log_info[1]):
                print("you are successfully logged in !")
            else :
                print("invalid username or passward , please try again")
                exit()
    else:
        exit()

    option_1=int(input(""" welcome in client system ^_^
    enter 1 :to add a jop post
    enter 2 :to remove a jop post
    enter 3 :to see the list of freelancers on the system
    enter 4 :see if they send a proposal or not
     and accept or reject proposal send by freelancer 
    """))
    if (option_1== 1):
        title = input("enter the title of post\n")
        jop_posts = input("enter the description of post :\n")
        post_id=input("enter the post id :\n")
        list_skills=input("enter the list of required skills :*notes you must separate each skill and last with (-) \n")
        list_skills.split("-")
        name = input("enter your name : \n")

        ##### to make a file to the description of post

        if os.path.exists(title) == False:
            main_dir = r'D:\pythonProject1\the system\jop'
            folder_path = title
            file_path = title + ".txt"
            folderpath_jop = os.path.join(main_dir, folder_path)
            fullpath_jop = os.path.join(main_dir, folder_path, file_path)
            os.mkdir(folderpath_jop)
            tit_jop = open(fullpath_jop, "a")
            tit_jop.write(title + "\n")
            tit_jop.write(jop_posts + "\n")
            tit_jop.write(post_id + "\n")
            tit_jop.write(str(list_skills.split("-")) + "\n")
            tit_jop.close()

            #### to make a file to the name of client
            m_dir = r'D:\pythonProject1\the system\jop'
            fo_path = title
            fi_path = 'the name of client.txt'
            full_fi_path = os.path.join(m_dir, fo_path, fi_path)
            client_name = open(full_fi_path, 'w')
            client_name.write(name + '\n')
            client_name.close()
        else:
            print("there are title job like this")




    elif (option_1== 2) :
        title=input("enter the title of post :")
        if (title in os.listdir(r'D:\pythonProject1\the system\jop')):
            maindir = r'D:\pythonProject1\the system\jop'
            foldernae = title
            filename = title + ".txt"
            folderpath = os.path.join(maindir, foldernae)
            fullpath = os.path.join(maindir, foldernae, filename)
            fullpath1=os.path.join(maindir, foldernae,"accepter.txt")
            fullpath2 = os.path.join(maindir, foldernae, "request.txt")
            fullpath3 = os.path.join(maindir, foldernae, "the name of client.txt")
            if os.path.exists(fullpath) == True:
                os.remove(fullpath)
            if os.path.exists(fullpath1) == True:
                os.remove(fullpath1)
            if os.path.exists(fullpath2) == True:
                os.remove(fullpath2)
            if os.path.exists(fullpath3) == True:
                os.remove(fullpath3)
            os.rmdir(folderpath)
        else:
            print("the title is not exist ")

    elif (option_1 ==3) : ### to print the name of freelancer in the system

        lis = []
        for i in os.listdir(r'D:\pythonProject1\the system\freelancer'):
            # print(i)
            lis.append(i)
        print(lis)

    elif (option_1 == 4) :

        accepter=input("you want to see if any one sent a request ?")
        if (accepter=='yes'):
            title = input("enter the title of post\n")
            maindir = r'D:\pythonProject1\the system\jop'
            foldernae = title
            filename = "request.txt"
            fullpath = os.path.join(maindir, foldernae, filename)
            if os.path.exists(fullpath)==True:
                with open(fullpath, 'r') as f:
                    for line in f:
                        print(line)
                accept = input("you accepted any one ?!")
                if (accept == 'yes'):
                    title = input("enter the title of post\n")
                    freelancer_id = input("enter the id of the freelancer accepted :\n")
                    maindir = r'D:\pythonProject1\the system\jop'
                    foldernae = title
                    filename = "accepter.txt"
                    fullpath = os.path.join(maindir, foldernae, filename)
                    x = open(fullpath, "a")
                    x.write(freelancer_id)
                    x.write("\n")
                    x.close()
            else:
                print("not exist")
        elif (accepter=='no'):
            print("you are existed")


############################## the system of freelancer #######################################

# the register of freelancers #
elif(option==2) :
    que = input("you have an account ?! yes or no ")
    if (que == "no"):
        username = input("enter the username :\n")
        pwd = input("enter the password :\n")
        id = input("enter the ID :\n")
        email = input("enter the email :\n")
        phone_number=input("enter your phone number :\n ")
        national_id=input("enter your national id :\n")
        maindir = r'D:\pythonProject1\the system\freelancer'
        foldernae = username
        filename = username + ".txt"
        folderpath = os.path.join(maindir, foldernae)
        fullpath = os.path.join(maindir, foldernae, filename)
        if os.path.exists(folderpath) == False:
            os.mkdir(folderpath)
            d = open(fullpath, "a")
            d.write(username)
            d.write(" ")
            d.write(pwd)
            d.write(" ")
            d.write(id)
            d.write(" ")
            d.write(email)
            d.write(" ")
            d.write(phone_number)
            d.write(" ")
            d.write(national_id)
            d.write("\n")
            d.close()
        else:
            print("this username are exist ")
            exit()

##### the login of freelancers #######

    elif (que=="yes") :
        username=input("enter the usernam : \n")
        passward=input("enter the passward : \n")
        id = input("enter the ID :\n")
        maindir = r'D:\pythonProject1\the system\freelancer'
        foldernae = username
        filename = username + ".txt"
        folderpath = os.path.join(maindir, foldernae)
        fullpath = os.path.join(maindir, foldernae, filename)
        for lines in open(fullpath,"r").readlines():
            log_info = lines.strip().split(" ")
            if (username ==log_info[0]) and (passward == log_info[1]):
                print("you are successfully logged in !")
            else :
                print("invalid username or passward , please try again")
                exit()
    else :
        exit()

    pro=input("have you made on any job before ?!")
    if (pro=='yes'):
        title = input("enter the title of post : \n")
        maindir = r'D:\pythonProject1\the system\jop'
        folder_path = title
        file_path ="accepter.txt"
        fullpath = os.path.join(maindir, folder_path, file_path)
        with open(fullpath, 'r') as p:
            for line in p:
                print(line)
    elif (pro=='no'):
        ##### to print a list of job
        lis_x=[]
        for x in os.listdir(r'D:\pythonProject1\the system\jop'):
            lis_x.append(x)
        print(lis_x)
        #### the jop that the freelancer are chosen
        title = input("enter the title of post : \n")
        for title1 in os.listdir(r'D:\pythonProject1\the system\jop'):

            if (title == title1):
                main_dir = r'D:\pythonProject1\the system\jop'
                folder_path = title
                file_path = title + ".txt"
                name='the name of client.txt'
                full_name=os.path.join(main_dir, folder_path,name)
                fullpath_jop = os.path.join(main_dir, folder_path, file_path)
                with open(full_name,'r') as x :
                    for lines in x :
                        print('the name of client'+lines)
                with open(fullpath_jop, 'r') as fp:
                    for line in fp:
                        print(line)
                proposal = input("you want to proposal in this job ?")
                if (proposal == 'yes'):
                    freelancer_id = input("enter your id :\n")
                    title = input("enter the title of post : \n")
                    job_id = input("enter the id of the job :\n")
                    skill_name = input("enter the skills you have :*notes you must separate each skill and last with (-)\n")
                    skill_name.split('-')
                    maindir = r'D:\pythonProject1\the system\jop'
                    foldernae = title
                    filename = "request.txt"
                    fullpath = os.path.join(maindir, foldernae, filename)
                    y = open(fullpath, "a")
                    y.write("the freelancer id : " + freelancer_id)
                    y.write(" ")
                    y.write("the job id : " + job_id)
                    y.write(" ")
                    y.write("the skill of freelancer :" +str(skill_name.split('-')))
                    y.write("\n")
                    y.close()
                    break
                else:
                    break
            # else:




#1
# file_pass1 = os.path.join(r"D:\pythonProject1\the system of user\user",file_pass)
            # print(file_pass1)
            # print(file_pass)
            # print(os.getcwd())
# os.chdir(r"the system of user\user\name")

#2
    # o = title + ".txt"     os.path.join(r"D:\pythonProject1\the system of user\jop", o)
#3
# r"D:\pythonProject1\the system of freelancer\freelancers"

#4
# print(lines)
# print(log_info)
# os.mkdir(username)

# 5
# o=title + ".txt"
            # title_pass = os.path.join(r"D:\pythonProject1\the system of user\jop",o)
            # os.mkdir(title)
# tit_jop=open(title_pass,"r")
# m=r'D:\pythonProject1\the system of user\jop\the title of jop'
        # file_jop="title.txt"
        # path_file=os.path.join(m,file_jop)
        # for i in os.listdir(r'D:\pythonProject1\the system of user\jop'):
        #     print(i)
 # maindir = r'D:\pythonProject1\the system of user\jop\the title of jop'
        # filename = "title.txt"
        # fullpath = os.path.join(maindir, filename)
        # title_p = open(fullpath, 'a')
        # title_p.write(title +"\n")
        # title_p.close()
 # dir=r'D:\pythonProject1\the system of freelancer\name of fl'
        # name="name.txt"
        # path_name=os.path.join(dir,name)
        # ff=open(path_name,'a')
        # ff.write(username+" ")
        # ff.close()

        # for lines in open(path_file,"r").readlines():
        #     info = lines.strip().split()
        #     print(info)
        #     for title in info:
        #         if (title in info):
        #             info.remove(title)
        #             maindir = r'D:\pythonProject1\the system of user\jop'
        #             foldernae = title
        #             filename = title + ".txt"
        #             folderpath = os.path.join(maindir, foldernae)
        #             fullpath = os.path.join(maindir, foldernae, filename)
        #             os.remove(fullpath)
        #             os.rmdir(folderpath)
        #             print("the post Successfully Deleted ")
        #             break
        #         else:
        #             print("the title is not exist ")
        #             break
        # for title in list_title :
        #     if (title in list_title ):
        #         list_title.remove(title)
        #         os.remove(title)
        #         print("the post Successfully Deleted ")
        #     else:
        #         print("the title is not exist ")
##########
# import itertools
# with open('myfile.txt', 'r') as f:
#  for line in itertools.islice(f, 12, 30):
# import os
# os.path.exists(name)
#  os.mkdir(name)
# if os.path.exists() == false
#