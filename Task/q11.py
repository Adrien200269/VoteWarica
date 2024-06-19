number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is divisible by 2.")
    if number % 4 == 0:
        print("The number is also divisible by 4.")
else:
    print("The number is not divisible by 2 or by 4.")


