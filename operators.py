#Working with operators in this
#Arithmetic vaiables
x=6
y=2
total=x+y
print("+",total)
total=x-y
print("-",total)
total=x/y
print("/",total)
total=x%y
print("%",total)
total=x/y
print("*",total)

##Comparison operators
a=30
b=60
out =(a<b)
print("<",out)
out =(a>b)
print(">",out)
out =(a==b)
print("==",out)
out =(a<=b)
print("<=",out)
out =(a>=b)
print(">=",out)

##Logical or | and
a=40
b=60
x=2
y=3


out =(a<b ) or (x>y)
print("Or",out)
out =(a<b) and (x>y)
print("And",out)
out =not(a<b)
print("Not",out)

#Membership operator asking
devops=("Linux","Vagrant","Bash","AWS","Jenkins","Ansible")
ans= "Bash"in devops
print("Membeship operator",ans)
