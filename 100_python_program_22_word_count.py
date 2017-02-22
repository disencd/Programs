'''
Programs:100_python_program_22_word_count.py
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''

def word_count_fun():
    word_dict = {}
    cnt = 0
    list = raw_input("Enter the Sentence : ").split(" ")
    print list
    for word in list:
        if word in word_dict.keys():
            word_dict[word] = list.count(word)
        else:
            word_dict[word] = 0

    word_dict.keys().sort()
    print (word_dict)


word_count_fun()
