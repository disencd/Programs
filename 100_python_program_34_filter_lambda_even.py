'''
Programs:100_python_program_34_filter_lambda_even.py
Question:
Write a program which can filter even numbers in a
list by using filter function. The list is:
[1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''

def filter_even(list):
    even = filter(lambda x : x % 2 == 0, list)

    print even

filter_even([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16])
