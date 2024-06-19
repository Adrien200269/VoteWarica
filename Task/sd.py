# def sum(a,b):
#     print(a+b)
#     print(a-b)
# sum(10,80)
# sum(90,10)


def sum(age,name):
    print(name,age)
sum(age="27",name="ram")

def sum(b,*a):
    print(a)
sum(10,20,30,40)


def sum(b,*a):
    print(a)
sum(10)

def sum(**a,):
    print(a)
sum(a=10,b=20,c=100)
