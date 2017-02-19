
'''
Programs:100_python_program_14_upper_lower_characters_cnt.py
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

dict = {"upperch":0, "lowerch":0}



for ch in raw_input("Enter ::: "):
    if ch.isupper():
        dict["upperch"] += 1
    if ch.islower():
        dict["lowerch"] += 1


print dict
