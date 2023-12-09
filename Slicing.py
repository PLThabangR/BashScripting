planet1 ="Closest to the sun"
print(planet1)

#The index of the string
print(planet1[0])
print(planet1[1])
print(planet1[2])
print(planet1[-2])
print(planet1[-1])
print("###################")
##Slicing a string
print(planet1[3:6])
print(planet1[1:5])
print(planet1[-10:])
print(planet1[8:10])

##Slicing a tuple
devops=("Linux","Vagrant","Bash","AWS","Jenkins","Ansible")
print(devops[-1])
print(devops[1:5])
print(devops[2:4][0])
print(devops[2:4][0][1:])

##Slicing the lis
print("This is the list slicing")
devops=["Linux","Vagrant","Bash","AWS","Jenkins","Ansible"]
print(devops[-1])
print(devops[1:5])
print(devops[2:4][0])
print(devops[2:4][0][1:])

#Dictionary Slicing
skills ={"devops":("Linux","Vagrant","Bash","AWS","Jenkins","Ansible"),"development":["Java","Node",".net","Python"]}

print(skills)
print(skills["devops"])
print(skills["development"])
print(skills["devops"][-1])
print(skills["devops"][2:4])
print(skills["devops"][4])
print(skills["development"])
print(skills["development"][-2][2])

