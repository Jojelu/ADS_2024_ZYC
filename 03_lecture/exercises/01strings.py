"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# Write your solution here

# string = input("Please enter a string:\n")
# amount = int(input("Please enter an amount:\n"))
# print(string*amount)

"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# Write your solution here
# word1 = input("Please enter a word:\n")
# word2 = input("Please enter another word:\n")
# if len(word1) > len(word2):
#     print(word1, "ist longer")
# elif len(word1) == len(word2):
#     print("The strings are equally long")
# else:
#     print(word2, "ist longer")

"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
str = input("String here: ")
for i in range(-1, -len(str) - 1, -1):
    print(str[i])

for i in range(len(str) - 1, -1, -1):
    print(str[i])

# Write your solution here
# string = input("Please enter a string:\n")
# for i in range(len(string)):
#     print(string[i])

# string = input("Please enter a string:\n")
# for i in range(-1, -len(string)-1, -1):
#     print(string[i])

""" 
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# Write your solution here
# string = input("Please enter a string:\n")
# if string[1] == string[-2]:
#     print("The second and the second to last characters are", string[1])
# else:
#     print("The second and the second to last characters are different.")
"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# Write your solution here
# width = int(input("Please enter a number for the width:\n"))
# print("#"*width)

"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# Write your solution here
# width = int(input("Please enter a number for width:\n"))
# height = int(input("Please enter a number for height:\n"))
# for i in range(height):
#     print("#"*width)

"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# Write your solution here
# string = input("Please enter a word of max. 20 characters:\n")
# factor = 20 - len(string)
# print("*"*factor + string)
"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre. 
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing
    
    ******************************
    *          testing           *
    ******************************

    Word: >> python
    
    ******************************
    *           python           *
    ******************************
"""
# Write your solution here
# word = input("Please enter a word of max. 28 characters:\n")
# frame_width = 30
# print("*" * frame_width)
# white_space = int(frame_width / 2 - int(len(word) / 2) - 1)
# print("*" + " "*white_space + word + " "*white_space + "*")
# print("*" * frame_width)
"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# Write your solution here
# string = input("Please enter a word:\n")
# for i in range(1, len(string)+1):
#     print(string[0:i])

"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# Write your solution here

# string = input("Please enter a word:\n")
# for i in range(len(string)-1, -1, -1):
#     print(string[i:])

"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# Write your solution here

# string = input("Please enter a word:\n")
# string = string.lower()
# if "a" in string:
#     print("a found")
# else:
#     print("a not found")
# if "e" in string:
#     print("e found")
# else:
#     print("e not found")
# if "o" in string:
#     print("o found")
# else:
#     print("o not found")

"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# Write your solution here

# string = input("Please enter a word:\n")
# starting_char = input("Please enter a character:\n")
# starting_index = string.find(starting_char)
# if len(string[starting_index:]) > 3:
#     print(string[starting_index:starting_index + 3])

"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here
string = input("Please enter a string:\n")
substring = input("Please enter a substring:\n")
start_index = string.find(substring)
end_index = start_index + len(substring)
substring_new = string[end_index:]
if substring in substring_new:
    print(substring_new.find(substring) + end_index)
else:
    print("The substring does not occur twice in the string.")