'''
Program : 100_python_program_33_repeated_ch.py
Create an algorithm to find the first non repetitive
character in words like
'television' and 'arizona'

'''

def repeat_character(word):
    unique_ch = {}
    for ch in word:
        if ch not in unique_ch.keys():
            unique_ch[ch] = 1
        else:
            print "Repeated Character " , ch


repeat_character("disencd is a programmer")
