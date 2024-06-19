# 1. print "softwarica" 10 times 
# for i in range(10):

#     print("softwarica")

# 2. Sum of a list 
# numbers = [1, 2, 3, 4, 5]  # Example list
# total = 0
# for num in numbers:
#     total += num
# print("The sum of the list is:", total)


# 3. print each character using indexing
# string = "softwarica"

# for i in range(len(string)):
# print(string[i])


# 4. write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
# given_list = [1, "a", "c", 2, 3, 4]

# print("Integers in the list are:")
# for item in given_list:
#     if isinstance(item, int):
#         print(item)

# 5.multiplication of a each element. given list=[4,5,3,2]

# given_list = [4, 5, 3, 2]
# product = 1

# for num in given_list:
#     product *= num

# print("The product of all elements in the list is:", product)

# 7. reverse a list
# given_list = [6, 9, 2, 5, 7]
# reversed_list = []

# for i in range(len(given_list) - 1, -1, -1):
#     reversed_list.append(given_list[i])

# print("Original list:", given_list)
# print("Reversed list:", reversed_list)

# 6. multiplication table of a given number
# number = int(input("Enter a number to print its multiplication table: "))

# print(f"Multiplication table of {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")

#question8:  given list is [1,2,3,4] but expected output in new list [2,3,4,5]
 
# list = [1,2,3,4]
# newList =[]
# for i in list:
#     newList.append(i+1)
# print(newList)
 
#question9: Given list is lst=[1,2,3,4] but print 1 and 4 only
# list = [1,2,3,4]
# for i in list:
#     if(i!=2 and i!=3):
#         print(i)
 
#question 10: Given list is lst=[1,2,3,4] but print 1 2 and 4 only
# list = [1,2,3,4]
# for i in list:
#     if(i!=3):
#         print(i)
 
#question11: Given list is [1,2,3,4] but expected output is [1,"a",2,4]
 
# list =[1,2,3,4]
# newList = []
# for i in list:
#     if i==3:
#         newList.append(2)
#     elif i==2:
#         newList.append("a")
#     else:
#         newList.append(i)
# print(newList)
 
#question 12:Given list is [1,2,3,4,5] separate the elements into odd and even categories.
# list=[1,2,3,4,5]
# odd=[]
# even=[]
 
# for i in list:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print('even',even)
# print('odd',odd)
 
#question 13: Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types
# list =  [1,2,3,"d",4,5,"a"]
# string =[]
# integer =[]
# for i in list:
#     if isinstance(i,int):
#         integer.append(i)
#     else:
#         string.append(i)
# print(string)
# print(integer)
 
#question14: Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
 
# list = [1,2,3,4,"a","b"]
# string =[]
# integer =[]
# for i in list:
#     if isinstance(i,int):
#         integer.append(i)
#     else:
#         string.append(i)
# print(string)
# print(integer)
 
#question 15: Python program that accepts a string and calculate the number of digits and letters and space
# input = str(input('Enter any thing: '))
# digits=0
# letters=0
# space=0
# for i in input:
#     if i.isspace():
#         space= space+1
#     elif i.isnumeric():
#         digits= digits+1
#     elif i.isalpha():
#         letters = letters+1
 
# print('spaces: ', space)
# print('number of digits: ', digits)
# print('number of letters: ',letters)
 
#question16: Python program to check the validity of username and password input by users
 
# username = 'sabja'
# password = 'sabja6969@'
# for i in range(1,4):
#    l_username = input('type for usename: ')
#    l_password = input('type your password: ')
#    if(username == l_username and password==l_password and '@' in password and len(l_password)>8 ):
#         print('you usename and password is valid')
#         break
#    else:
#      print('your username and password isnot valid')


#Question 17. program to print the given number is odd or even


# while True:
#     try:
#         num = int(input("Enter a number (or type 'exit' to quit): "))
#         if num % 2 == 0:
#             print(f"{num} is even.")
#         else:
#             print(f"{num} is odd.")
#     except ValueError:
#         print("Exiting the program.")
#         break


#Question 20. Given list is lst=[1,2,3,4] but print 1 and 2 only


# list = [1,2,3,4]
# for i in list:
#     if(i!=4 and i!=3):
#         print(i)

#question 18: factorial of a given number
# num=7
# factorial =1
# for i in range(1,num+1):
#     factorial = factorial*i
# print(factorial)
 
#question19: Print multiplication table of  1,2,3,4,5,6,7,8
# list =[1,2,3,4,5,6,7,8]
# for i in list:
#     for j in range(1,11):
#         print(i,'*',j,'=',i*j)
#     print(' ')

#question21:  Python program to calculate the sum of all the odd numbers within the given range
# sum=0
# for i in range(0,15):
#     if(i%2!=0):
#         sum = sum +i
# print(sum)
 
#question22: Python program to calculate the sum of all the even numbers within the given range.
# sum=0
# for i in range(0,15):
#     if(i%2==0):
#         sum = sum +i
# print(sum)
 
#question23: Python program to count the space of a given string
# string = "i am a program"
# space_count=0
# for i in string:
#     if i.isspace():
#         space_count=space_count+1
# print(space_count)
 
#question 24: given list is [1,2,3,4] but expected output is [1,8,27,64]
# list = [1,2,3,4]
# output =[]
# for i in list:
#     output.append(i**3)
# print(output)
 
#question25:  reverse of a string a="programming"
# a="programming"
# for i in range(len(a)-1,-1,-1):
#     output=a[i]
#     print(output)
 
#question26: Place a break statement in the for loop so that it prints from 0 to 7 only (including 7). Given range(50)
 
# for i in range(50):
#     if i >7:
#         break
#     else:
#         print(i)
 
#question 27: Write a for loop that iterates through a string and prints every character.
# string='programming'
# for i in string:
#     print(i)
 
#question28: Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". Hint a=["ram","shyam",1,2] expected output:  Hello!ram Hello!shyam
# list = ['shyam','ram','sabja']
# for i in list:
#     print(f'Hello!,{i}')
 
#question 29:Using a for loop and .append() method append each item with a Dr. prefix to the lst. Hint a=["ram","shyam"] expected output:  ['Dr.ram', 'Dr.shyam','Dr.1','Dr.2']
# list=['ram','hari','shyam']
# new_list=[]
# for i in list:
#     new_list.append(f'Dr.{i}')
# print(new_list)
 
#question30:  Write a for loop which appends the square of each number to the new list.
# list=[1,2,3,4,5,6,7,8,9]
# new_list=[]
# for i in list:
#     square = i**2
#     new_list.append(square)
# print(new_list)
 
#question 31: Write a for loop using an if statement, that appends each number to the new list if it's positive. given lst1=[111, 32, -9, -45, -17, 9, 85, -10]
# list=[111, 32, -9, -45, -17, 9, 85, -10]
# new_list=[]
# for i in list:
#     if i>0:
#         new_list.append(i)
# print(new_list)
 
#question32: Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. given list=[0,1,2,3,4,5,6]
# list=[0,1,2,3,4,5,6]
# for i in list:
#     if i!=3 and i!=6:
#         print(i)

#question 33: Write a for loop which appends the type of each element in the first list to the second list.
# list =[1,2,'one',[1,2,3]]
# new_list=[]
# for i in list:
#     new_list.append(type(i))
# print(new_list)
 
#question34:  Use else block to display a message “Done” after successful execution of for loop.
# for i in range(10):
#     print(i)
# else:
#     print('Done')
 
#question35: Write a for loop statement to print the following series:
#105 98 -------7
# for num in range(105, 6, -7):
#     print(num, end=" ") 
 
#question 36: removal bad characters from the given string. Given bad_chars = [';', ':', '!', "*"], string = "py;th* o:n ! ;py * t*h:o !n".  Expected output = pythonpython
# list=[';', ':', '!', "*"," "]
# string = "py;th* o:n ! ;py * t*h:o !n"
# output=""
# for i in string:
#     if i not in list:
#         output += i
# print(output)


# Question 37. Python program to count the number of even and odd numbers from a series of numbers.  


# numbers = [10, 23, 36, 41, 52, 65, 78, 89, 90, 101]

# even_count = 0
# odd_count = 0

# # Loop through each number in the list
# for number in numbers:

#     if number % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Number of even numbers:", even_count)
# print("Number of odd numbers:", odd_count)

# Question No. 38. Write a python program to display all the prime numbers within a given range.
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers_in_range(start, end):
#     primes = []
#     for num in range(start, end + 1):
#         if is_prime(num):
#             primes.append(num)
#     return primes

# start = 10
# end = 50

# primes = prime_numbers_in_range(start, end)
# print(f"Prime numbers between {start} and {end}: {primes}")

# Question 39. given number is prime or not

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# number = 29

# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# Question 40. program to check given number is palindrome or not

# def is_palindrome(num):
#     num_str = str(num)
#     start = 0
#     end = len(num_str) - 1
#     while start < end:
#         if num_str[start] != num_str[end]:
#             return False
#         start += 1
#         end -= 1
#     return True

# number = 12321

# if is_palindrome(number):
#     print(f"{number} is a palindrome.")
# else:
#     print(f"{number} is not a palindrome.")


#Question 41. program to check given number is armstrong or not

# def is_armstrong_number(num):
#     num_str = str(num)
#     num_digits = len(num_str)
#     armstrong_sum = 0
#     for digit in num_str:
#         digit_int = int(digit)
#         armstrong_sum += digit_int ** num_digits
#     return armstrong_sum == num

# number = 153

# if is_armstrong_number(number):
#     print(f"{number} is an Armstrong number.")
# else:
#     print(f"{number} is not an Armstrong number.")

#Question 42.  python program to check a number is perfect number


# def is_perfect_number(num):
#     if num <= 0:
#         return False
    
#     divisor_sum = 0
    
#     for divisor in range(1, num // 2 + 1):
#         if num % divisor == 0:
#             divisor_sum += divisor
    
#     return divisor_sum == num

# number = 28

# if is_perfect_number(number):
#     print(f"{number} is a perfect number.")
# else:
#     print(f"{number} is not a perfect number.")
