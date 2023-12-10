#Python built in functions
#
#String methods
message="seek first the kingdom of God and his righteousness then all will be added to you"
print(message)
print(message.capitalize())
print(message.upper())

#dir()
print(dir(message))
#Define a function
def add(var1,var2):
    total=var1+var2
    return total
print("The sum is",add(4,5))

def summ(args):
    x=0
    for i in args:
        x+=i
    return x
results = summ([23,45,67,7,8,23])
print(results)

#default
def greetings(msg="morning"):
    print("GOOD",msg)
    print("Welcome to the family")
greetings()

def vaccine_feedback(vac,efficacy):
    print("The",vac,"vaccine is having",efficacy,"% efficacy")
    if(efficacy >50) and (efficacy<=75):
        print("The vaccine seem effective,Needs more trials")
    elif (efficacy >75) and (efficacy<=100):
          print("Consider this vaccine")
    else :
        print("Needs many more trails")
vaccine_feedback("AstraZencar",60)
