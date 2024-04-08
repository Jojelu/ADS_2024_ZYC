"""
Write a program which asks the user for a number.
The program then prints out the number multiplied by five.
Example:
    Please type in a number: >> 7
    7 times 5 is 35
"""
# Write your solution here
# number1 = input("Please enter a number:\n")
# number2 = int(number1)*5
# print(f"{number1} times 5 is {number2}")

number = input("Please enter a number:\n")
print(number, "times 5 is", int(number) * 5)
"""
Write a program which asks the user for their name and year of birth. 
The program then prints out a message as follows:
    What is your name? >> Frances Fictitious
    Which year were you born? >> 1990
    Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
"""
# Write your solution here
name = input("What is your name?\n")
year_birth = int(input("Which year were you born?\n"))
age = 2024 - year_birth
print(f"Hi {name}, you will be {age} years old at the end of the year 2024")
"""
Write a program which asks the user for a number of days. 
The program then prints out the number of seconds in the amount of days given.
Example:
    How many days? >> 7
    Seconds in that many days: >> 604800
"""
# Write your solution here
numDD = int(input("How many days?\n"))
numSec = numDD * 3600 * 24
print("Seconds in that many days:", numSec)


"""
This program asks the user for three numbers. 
The program then prints out their product, that is, the numbers multiplied by each other. 
There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it. 
Please fix it.
"""
# Fix the code
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number1 * number2 * number3

print("The product is", product)


"""
Write a program which asks the user for four numbers. 
The program then prints out the sum and the mean of the numbers.
Example: 
    Number 1: >> 2
    Number 2: >> 1
    Number 3: >> 6
    Number 4: >> 7
    The sum of the numbers is 16 and the mean is 4.0
"""
# Write your solution here
number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
number4 = int(input("Please type in the fourth number: "))
sum = number1 + number2 + number3 + number4
mean = sum / 4

print(f"the sum of the numbers is {sum} and the mean of them is {mean}")


"""
Write a program that asks the user for a three-digit number input.
Reverse the given number by using modulo and division operator.
Example:
    Enter a number: >> 123
    The reversed number is: >> 321
"""
# Write your solution here
num3d = int(input("Please enter a three-digit number\n"))
numL = int(num3d / 100)
numR = int(num3d % 10)
numM = int(num3d % 100 / 10)
num3R = numR * 100 + numM * 10 + numL
print ("The reversed number is:", num3R)
