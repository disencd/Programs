'''
Program : 100_python_program_1000_3000_even_no
Question:

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

list = [x for x in xrange(1000,1200) if int(x) % 2 == 0 ]

print(list)
