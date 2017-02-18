"""
Program : 100_python_program_6_formula
Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
"""

import math

def input_formula(list):
    c = 50
    h = 30
    q = []
    for d in list:
        q.append(math.sqrt((2 * c * int(d)) / h))

    return q

list = raw_input().split(",")
q = input_formula(list)

print (q)
