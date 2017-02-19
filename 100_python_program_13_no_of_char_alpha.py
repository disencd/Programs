
'''
Program : 100_python_program_13_no_of_char_alpha.py
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

dict = {"char":0, "int":0}



for ch in raw_input("Enter ::: "):
    if ch.isalpha():
        dict["char"] += 1
    if ch.isalpha():
        dict["int"] += 1


print dict
