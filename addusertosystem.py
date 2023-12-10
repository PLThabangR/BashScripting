#!/usr/bin/python2
import os

userlist =["alpha","beta","gamma"]

print("Adding user to the system using python ")
print("####################################################")

for user in userlist:
    existcode= os.system("id {}".format(user))
    if existcode !=0:
        print("User",user,"does not exit.Adding it")
        print("################################")
        print("e")
        os.system("useradd {}".format(user))
    else:
        print("User already exist ,skipping it")
        print("################################")
        print()

##Adding user to the group
exitcode = os.system("grep science /etc/group")
if existcode != 0:
    print("Group science does not exist.Adding it")
    print("#########################")
    print()
    os.system("groupadd science")
else:
    print("Group already exist.skipping it")
    print("#########################")
    print()