#taking num and operator from user
firstNum= int(input('Enter First Number: '))
secondNum= int(input('Enter Second Number: '))
ope= input('Enter a operator: ')
b={ '+':firstNum+secondNum, '-':firstNum-secondNum, '*':firstNum*secondNum, '/': firstNum/secondNum}
if(ope in b):
    print(b[ope])
else:
    print("Invalid Operator!!")