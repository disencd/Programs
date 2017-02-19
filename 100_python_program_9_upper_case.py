'''
Program : 100_python_program_9_upper_case.py
Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

'''

list = []
while(1):
    x = raw_input()

    if x:
        list.append(x.upper())

    else:
        break


print(list)
