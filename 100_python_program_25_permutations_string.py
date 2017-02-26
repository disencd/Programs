'''
Programs:100_python_program_25_permutations_string.py
Checking if two strings are permutations of each other in Python
'''

def permutation(str1, str2):
    str_dict = {}

    for ch in str1:
        if ch in str_dict.keys():
            str_dict[ch] += 1
        else:
            str_dict[ch] = 1


    for ch in str2:
        if ch in str_dict.keys():
            str_dict[ch] -= 1
        else:
            return -1

    if str_dict.values() == 0:
        return 0
    else:
        return -1


val = permutation("acbcsccc","abc")
print(val)
