'''
Program: input_validation_while_loops_assignment.py
Author: Joshua M. McGinley
Last date modified: 09/28/2022

Write a small script, input_while.py that prompts the user for numeric input between 1 and 100. Prompt the user
until the input is in the correct range. Once a the input is correct, store the input in a list.
Script pseudocode:
declare a list variable
prompt and get the user input
while user input is not good (in range)
     prompt user for good input
store in list
print the list
That's not useful! You need multiple inputs from the user,

declare a list variable

declare a sentinel value for user input

prompt get the user input (indicating sentinel value to stop)

while sentinel value is not stopping value
      while user input is not good (in range)
            prompt user for good input
      store in list
      prompt and get the next user input

print the list using a for loop



Test running your script in the shell.
Add doctring to the top of your file, add comments at the bottom with your tests and observed output after a few
test runs of your code.
Submit you .py file.
'''

the_list = []
sentinel = 666
yrNum = int(input('Enter number between 1-100 (enter 666 to stop): '))
while (yrNum != sentinel):
    while yrNum < 1 or yrNum > 100:
        try:
             yrNum = int(input('Enter number between 1-100 (enter 666 to stop): '))
        except:
            print('Evil input!')
    the_list.append(yrNum)
    yrNum = int(input('Enter number between 1-100 (enter 666 to stop): '))

for x in range(len(the_list)):
    print(the_list[x])


