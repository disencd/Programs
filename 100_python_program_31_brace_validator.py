'''
Programs:100_python_program_31_brace_validator.py
Question:
Validate braces - {} () []
bug - ()) - wont work
'''

def brace_validator(str):

    brace_dict = {'{':'}', '[':']', '(':')'}
    brace_list = []

    for val in str:

        if val in brace_dict.keys():
            print "Appending"
            brace_list.append(brace_dict[val])

        elif val in brace_list:
            print "Popping"
            brace_list.pop()

    if brace_list:
        return -1


print "Validator " , brace_validator("{disen [is (CD) {Wowww}]}")
