__author__ = 'c_disenc'

def file_operations_read_linebyline(log):
    with open(log) as fh:
        for line in fh:
            print(line)

def file_operations_stripnewline(log):
    with open(log) as fh:
        for line in fh:
            print(line[:-1])

def file_operations_firstword_of_eachline(log):
    with open(log) as fh:
        for line in fh:
            word = line.split(" ")
            print(word[0])

#file_operations_read_linebyline("telecan_logs")

#file_operations_stripnewline("telecan_logs")

file_operations_firstword_of_eachline("telecan_logs")
