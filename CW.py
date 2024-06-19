day =int(input("Enter a number upt 7: "))
if(day==1):
    print("Sunday!")
elif(day==2):
    print("Monday!")
elif(day==3):
    print("Tuesday!")
elif(day==4):
    print("Wednesday!")
elif(day==5):
    print("Thursday!")
elif(day==6):
    print("Friday!")
elif(day==7):
    print("Saturday!")
else:
    print(day)
#using dic
a={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
if(day in a):
    print(a[day])
else:
    print(day)

#taking num and operator from user
firstNum= int(input('Enter First Number: '))
secondNum= int(input('Enter Second Number: '))
ope= input('Enter a operator: ')
b={ '+':firstNum+secondNum, '-':firstNum-secondNum, '*':firstNum*secondNum, '/': firstNum/secondNum}
if(ope in b):
    print(b[ope])