'''
Program : 100_python_program_8_word_sorting
Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

'''

items=[x for x in raw_input().split(',')]
print(items)
items.sort()
print ','.join(items)
