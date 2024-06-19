# a="ram"
# b=0
# for i in range(10):
#     print(i, "=",a[i])
#     b=b+1

# a=5
# for i in range(1, 11):
#     print(a,'*','i','=',a*i)


username= (input('Give your username: '))
password=(input('Give your password: '))
for i in range(1,4):
    username1= (input('Give your valid username: '))
    password1=(input('Give your valid password: '))

    if(
        username != username1
        or password != password1
        or len(password) < 8
    ):
        if i == 3:
            continue 
        print(3 - i,"attempts left!!")
    else:
        print("You have sucessfully entered!")
        break
else:
        print("You have been Blocked!!!")
  