"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
# Write your solution here
number = int(input("Please enter a number \n"))
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd")

"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# Write your solution here
grade = int(input("Please enter your exam grade here without the percentage sign \n"))
if grade < 60:
    print("Unfortunately, you failed the exam.")
elif 60 <= grade < 90:
    print("You passed the exam!")
else:
    print("You are excellent!")
"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
# Write your solution here
while True:
     food = str(input("Would you like a sandwich, salad, or wrap?\n"))
     if food == "sandwich" or food == "salad" or food == "wrap":
        break
     print("Invalid input, please try again!")

if food == "sandwich":
    while True:
        sandwich_type = input("What kind of sandwich would you like: chicken, beef, veggie?\n")
        if sandwich_type == "chicken" or sandwich_type == "beef" or sandwich_type == "veggie":
            break
        print("Invalid input, please try again!")
    if sandwich_type == "chicken":
        print("Your order: Chicken sandwich")
    elif sandwich_type == "beef":
        print("Your order: Beef sandwich")
    else:
        print("Your order: Veggie sandwich")
elif food == "salad":
    while True:
        dressing_type = input("What kind of dressing would you like: vinaigrette, ranch, or caesar?")
        if dressing_type == "vinaigrette" or dressing_type == "ranch" or dressing_type == "caesar":
            break
        print("Invalid input, please try again!")
    if dressing_type == "vinaigrette":
        print("Your order: Salad with vinaigrette dressing")
    elif dressing_type == "ranch":
        print("Your order: Salad with ranch dressing")
    else:
        print("Your order: Salad with caesar dressing")
else:
    toasted = input("Do you want it toasted? Enter yes or no\n")
    if toasted == "yes":
        print("Your order: Toasted wrap")
    else:
        print("Your order: a wrap")