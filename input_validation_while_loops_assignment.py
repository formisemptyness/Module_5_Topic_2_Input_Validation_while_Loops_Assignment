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
range1 = range(1, 101)
sentinel = "continue"
yrNum = 0

sentinel = (input('Enter exit to quit: '))

while (sentinel != "exit"):
    yrNum = 0
    while (yrNum not in range1):
        try:
            yrNum = int(input('Enter an integer between 1-100: '))
        except:
            print('Bad input!')
    print('Thank you.')
    the_list.append(yrNum)
    sentinel = (input('Enter exit to quit: '))

for x in range(len(the_list)):
    print(the_list[x])


#
#Enter exit to quit: g                #  Enter exit to quit: jkl;
#Enter an integer between 1-100: 75   #  Enter an integer between 1-100: 10
#Thank you.                           #  Thank you.
#Enter exit to quit: 200              #  Enter exit to quit: jh
#Enter an integer between 1-100: 500  #  Enter an integer between 1-100: 11
#Enter an integer between 1-100: 700  #  Thank you.
#Enter an integer between 1-100: 10   #  Enter exit to quit: kkm
#Thank you.                           #  Enter an integer between 1-100: 12
#Enter exit to quit: exit             #  Thank you.
#50                                   #  Enter an integer between 1-100: 13
#75                                   #  Thank you.
#10                                   #  Enter exit to quit: jk
#                                     #  Enter an integer between 1-100: 105
#Process finished with exit code 0    #   Enter an integer between 1-100: 15
#                                     #   Thank you.
#                                     #  Enter exit to quit: exit
#                                     #  10
#                                     #  11
#                                     #  12
#                                     #  13
#                                     #  15
#
#
