'''
Programs:100_python_program_15_add_number_a+aa+aaa+aaaa.py
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

'''

user_input = raw_input()

num_var = temp_num_var = 4
sum = 0
variable = ""

for val in range(num_var,0,-1):
    while(num_var > 0):
        variable = variable + user_input
        num_var -= 1

    sum += int(variable)
    print (variable + " + ")
    temp_num_var -= 1
    variable = ""
    num_var = temp_num_var


print sum
