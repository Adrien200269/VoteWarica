# # Question1 Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3"
# a=2
# b=4
# if a==b:
#     print("1")
# elif a>b:
#     print("2")
# else:
#     print("3")

#Question2 Print "Hello" if a is equal to b, or if c is equal to d.
# a=2
# b=3
# c=4
# d=4
# if a==b or c==d:
#     print("Hello")

#Question3 Print "Hello" if a is equal to b, and c is equal to d.
# a=2
# b=2
# c=4
# d=4
# if a==b and c==d:
#     print("Hello")

#Question4 For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.
# a=0
# if a>0:
#     print('True')
# elif a<0:
#     print('False')
# else:
#     print('Zero')

#Question5 Check whether the user input number is even or odd and display it to user.
# a= 4
# if a % 2==0:
#     print("Even")
# else:
#     print("Odd")

#Question6 WAP which accepts marks of four subjects and display total marks, percentage and grade.
# Design=90
# Algorithm=80
# Maths=70
# Data=60
# Total_marks=Design+Algorithm+Maths+Data
# print(Total_marks)
# Percentage=(Total_marks/400)*100
# print(Percentage)
# if Percentage>70:
#     print("Distinction")
# elif Percentage>60:
#     print("First Division")
# elif Percentage>40:
#     print("Pass")
# else:
#     print("Fail")

#Question7 What is the output of ‘APPLE’ > ‘apple’?
#False

#Question8 Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
# Cost price(in Rs)                  Tax
# >100000                              15%
# >50000 and <=100000      10%
# <=50000                               5%

# bike=int(input("enter the price of bike: "))
# if bike>100000:
#     print("15%")
# elif bike>50000 and bike<= 100000:
#     print("10%")
# else:
#     print("5%")

#Question9 9. Accept the age of 4 people and display the youngest one.
# a=int(input("Enter a age: "))
# b=int(input("Enter another age: "))
# c=int(input("Enter another age: "))
# d=int(input("Enter another age: "))

# youngest_age = min(a, b, c, d)

# print("The youngest person is {} years old.".format(youngest_age))

#Question10 Accept the age of 4 people and display the oldest one.
# a=int(input("Enter a age: "))
# b=int(input("Enter another age: "))
# c=int(input("Enter another age: "))
# d=int(input("Enter another age: "))

# oldest_age = max(a, b, c, d)

# print("The oldest person is {} years old.".format(oldest_age))\

# Question 11 Accept the grades from the user and display the grade according to the following criteria:
# Below 25 --D
# 25 to 45  -- C
# 45 to 50 -- B
# 50 to 60 --B+
# 60 to 80 -- A
# Above 80 -- A+

# grade = float(input("Enter the grade: "))

# if grade < 25:
#     result = "D"
# elif 25 <= grade < 45:
#     result = "C"
# elif 45 <= grade < 50:
#     result = "B"
# elif 50 <= grade < 60:
#     result = "B+"
# elif 60 <= grade < 80:
#     result = "A"
# else:
#     result = "A+"

# print("Grade:", result)

#question12 A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years            10%
# >=6 and <=10                       8%
# Less than 6 years                5%

# time = float(input("Enter the number of years of service: "))

# if time > 10:
#     print ("10%")
# elif 6 <= time <= 10:
#     print ("8%")
# else:
#     print ("5%")

#Question 14 Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day 

# num_days = int(input("Enter the number of days: "))

# if num_days > 15:
#     charge_per_day = 5
# elif num_days >10:
#     charge_per_day = 4
# elif num_days >5 :
#     charge_per_day = 3
# else:
#     charge_per_day = 2

# total_charge = num_days * charge_per_day

# print("The total charge for {} days is Rs.{}".format(num_days, total_charge))

#Question 15 A company decided to give bonus of 5% to employee if his/her year of service is more than 5years. Ask user for their salary and year of service and print the net bonus amount.
# salary = float(input("Enter the employee's salary: "))
# years_of_service = int(input("Enter the number of years of service: "))

# if years_of_service > 5:
#     bonus_percentage = 5
#     net_bonus = (bonus_percentage / 100) * salary
#     print("Congratulations! You are eligible for a {}% bonus.". format(bonus_percentage))
#     print("Net bonus amount: Rs. ", net_bonus)
# else:
#     print("Sorry, you are not eligible for a bonus.")

# Question 16 


#Question 17. Write a Python program to display your details like name, age, address in three different lines.
# name = "Sabja"
# age = 21
# address = "Baneshwor"

# print("Name:", name)
# print("Age:", age)
# print("Address:", address)

#Question18 Write a python program which accepts the radius of circle from user and compute the area.

# radius = float(input("Enter the radius of the circle: "))

# area = 3.1 * radius ** 2

# print("The area of the circle is:", area)

#Question19  A school decided to replace the desks in three classrooms. Each desk sits two students. Given the number of students in each class, print the smallest possible number of desks that can be purchased. The program should read three integers: the number of students in each of the three 
# classes, a, b and c respectively.

# a=int(input("Enter the students of First class: "))
# b=int(input("Enter the students of Second class: "))
# c=int(input("Enter the students of Third class: "))
# a=20
# b=21
# c=22
# desk=2
# required_desk=(a+b+c)//2
# print("The required desk is ",required_desk)


#Question 20 N students take K apples and distribute them among each other evenly. The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket? The program reads the numbers N and K. It should print the two answers for the questions above.


# num_students = int(input("Enter the number of students: "))
# total_apples = int(input("Enter the total number of apples: "))

# apples_per_student = total_apples // num_students
# apples_remainder = total_apples % num_students

# print("Each student will get", apples_per_student, "apples.")
# print("There will be", apples_remainder, "apples remaining in the basket.")

#Question 21 repeated on 12

#Question22 Accept three numbers from the user and display the second largest number.
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     if num2 >= num3:
#         second_largest = num2
#     else:
#         second_largest = num3
# elif num2 >= num1 and num2 >= num3:
#     if num1 >= num3:
#         second_largest = num1
#     else:
#         second_largest = num3
# else:
#     if num1 >= num2:
#         second_largest = num1
#     else:
#         second_largest = num2
# print("The second largest number is:", second_largest)

#Question23. Write a program to check whether a person is eligible for voting or not. (accept age from user)

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote yet.")

#Question24 Write a program to check whether a number is divisible by 7 or not.
# number = int(input("Enter a number: "))

# if number % 7 == 0:
#     print(number, "is divisible by 7.")
# else:
#     print(number, "is not divisible by 7.")

#Question25 

#Question26. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
# number = int(input("Enter a number: "))

# if number % 2 == 0:
#     print("The number is divisible by 2.")
#     if number % 4 == 0:
#         print("The number is also divisible by 4.")
# else:
#     print("The number is not divisible by 2 or by 4.")

#Question 27. Write a program to accept two numbers and mathematical operators and perform operation accordingly.

# firstNum= int(input('Enter First Number: '))
# secondNum= int(input('Enter Second Number: '))
# ope= input('Enter a operator: ')
# b={ '+':firstNum+secondNum, '-':firstNum-secondNum, '*':firstNum*secondNum, '/': firstNum/secondNum}
# if(ope in b):
#     print(b[ope])
# else:
#     print("Invalid Operator!!")

#Question 29 Accept the following from the user and calculate the percentage of class attended:

# a. Total number of working days
# b. Total number of days for absent
# After calculating percentage show that, if the percentage is less than 75, than student will not be able to sit in exam. 

# total_working_days = int(input("Enter the total number of working days: "))
# days_absent = int(input("Enter the total number of days absent: "))

# days_attended = total_working_days - days_absent

# attendance_percentage = (days_attended / total_working_days) * 100

# print("Attendance Percentage: ",attendance_percentage)

# if attendance_percentage < 75:
#     print("The student will not be able to sit in the exam.")
# else:
#     print("The student is eligible to sit in the exam.")


#Question30 Write a program to accept percentage and display the category according to the following criteria:
# Percentage                                   Category
# <40                                              Failed
# >=40 and <55                             Fair
# >=55 and <65                             Good
# >=65                                            Excellent

# percentage = float(input("Enter the percentage: "))

# if percentage < 40:
#     category = "Failed"
# elif 40 <= percentage < 55:
#     category = "Fair"
# elif 55 <= percentage < 65:
#     category = "Good"
# else:
#     category = "Excellent"

# print("The category is",category)


#Question 31 31. Accept the age, gender('M', 'F'), number of days and display the wages accordingly.
# Age                       Gender    Wage/day
# >=18 and <30      M             700
#                               F              750
# >=30 and <=40    M             800
#                               F              850

# age = int(input("Enter the age: "))
# gender = input("Enter the gender (M/F): ")
# number_of_days = int(input("Enter the number of working days: "))


# if 18 <= age < 30:
#     if gender == 'M':
#         wage_per_day = 700
#     elif gender == 'F':
#         wage_per_day = 750
# elif 30 <= age <= 40:
#     if gender == 'M':
#         wage_per_day = 800
#     elif gender == 'F':
#         wage_per_day = 850
# else:
#     print("Age out of the specified range for wage calculation.")

# if number_of_days>0:
#     total_wages = wage_per_day * number_of_days
#     print(f"The total wages for {number_of_days} days is: {total_wages}")
# else:
#     print("Wage per day could not be determined due to invalid age or gender input.")

#Question 32 Repeated at 22

#Question 33

# a=True
# b=True
# c=True
# d=True

# print(c)
# print(d)
# print(not a)
# print(not b)
# print(not c)
# print(not d)
# print(a and b)
# print(a or b)
# print(a and b or c)
# print(not a or b or c)
# print(not a or not b or not c)
# print(not(not a or not b or not c))

#Question 34 Accept input from user
# if given number is a multiple of both 3 and 5 prints "FizzBuzz" instead of number
# if  given number is a multiple of 3 but not 5 prints "Fizz" instead of number
# if given number is a multiple of 5 but not 3 prints "Buzz" instead of number
# if given number is not multiple of 3 or 5 prints value as usual. 


# number = int(input("Enter a number: "))

# if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
# elif number % 3 == 0:
#     print("Fizz")
# elif number % 5 == 0:
#     print("Buzz")
# else:
#     print(number)


#Question 35 
i=3
j=5
k=7
if i<j:
    if j<k:
        i=j
    else:
        j=k
else:
 if j>k:
    j=i
 else:
    i=k
print(i,j,k)



