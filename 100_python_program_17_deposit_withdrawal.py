'''
Programs:100_python_program_17_deposit_withdrawal.py
Question:
Write a program that computes the net amount of a
bank account based a transaction log from
console input. The transaction log format is
shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied
to the program:
D 300
D 300
W 200
D 100
Then the output should be:
500

'''
sum = 0

while(1):
    inp = raw_input()

    if inp:
        list = inp.split(" ")
        print list
        if list[0] == "D":
            sum += int(list[1])

        elif list[0] == "W":
            sum -= int(list[1])

        else:
            break

    else:
        break

print(sum)
