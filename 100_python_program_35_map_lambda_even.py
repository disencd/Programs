'''
Programs:100_python_program_35_map_lambda_even.py
Question:
Write a program which can filter even numbers in a
list by using filter function. The list is:
[1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.
'''

def filter_even(list):
    sqr = map(lambda x : x ** 2, list)

    print sqr

filter_even([1,2,3,4,5,6,7,8,9,0,11,12,13,14,15,16])
