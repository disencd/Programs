'''
Programs:100_python_program_36_palindrome.py
palindrome program
'''

def palindrome():
    while(1):
        inp = raw_input("Enter the string : ")

        if inp == ''.join(reversed(inp)):
            print("Palindrome ")
        else:
            print("Not Palindrome ")

palindrome()
