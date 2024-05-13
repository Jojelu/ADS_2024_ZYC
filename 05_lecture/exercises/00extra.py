"""
Advanced Exercises, focussing on Lists
"""

"""
### Exercise 1: List Filtering ###

Write a program that initializes a list of integers. Use a loop to fill the list with numbers from 1 to 20.
Then, using list comprehension, create a new list that only includes even numbers from the original list.
Print the original and the filtered lists.

Example Output:
    Original list: [1, 2, 3, ..., 20]
    Filtered list: [2, 4, 6, ..., 20]
"""

# Write your solution here
mylist = []
for i in range(1, 21):
    mylist.append(i)
print(mylist)
new_list = mylist

for i in range(1, 21):
   if i % 2 == 1:
     new_list.remove(i)
print(new_list)

"""
### Exercise 2: Todo List Application ###

Create a simple todo list application. Start with an empty list named "todos". 
Allow the user to continuously add new tasks to the list by typing them into the console. 
The user can also type 'done' to stop adding tasks, 'remove' to remove the last task, or 'view' to display all tasks.
Use a loop to handle these inputs and modify the list accordingly. 
If 'done' is typed, print the final list of tasks and exit the loop.

Example Interaction:
    Please enter a task or command: >> Buy milk
    Task added.
    Please enter a task or command: >> Do homework
    Task added.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk', 'Do homework']
    Please enter a task or command: >> remove
    Last task removed.
    Please enter a task or command: >> view
    Current tasks: ['Buy milk']
    Please enter a task or command: >> done
    Final tasks: ['Buy milk']
    Exiting...
"""
mylist = []
while True:
    user_input = input("please enter a task or command:\n")
    if user_input == "remove":
        mylist.pop(len(mylist)-1)
        print("Last task removed")
    elif user_input == "view":
        print("Current tasks:", mylist)
    elif user_input == "done":
        print("Final tasks:", mylist)
        break
    else:
        mylist.append(user_input)
        print("Task added.")








# Write your solution here

"""
### Exercise 3: Analyzing Numbers ###

Create a program that initializes a list with numbers (you can hard code them or get them from the user).
Write a function that receives this list and returns a new list with the following items:
    - 'max': Maximum value in the list
    - 'min': Minimum value in the list
    - 'average': Average of the numbers
    - 'under_avg': A new list inside the list, containing the numbers from the original list that are below the average
Use loops and conditionals to compute these values and store them in the new list.
Print the list at the end.

Example Input: [1, 2, 3]
Example Output: [3, 1, 2, [1]]

BONUS TASK:
If you want, you can research "dictionaries" in Python and structure your solution like that:
    {
        'max': 3,
        'min': 1,
        'average': 2,
        'under_avg': [1]
    }
"""

# Write your solution here
