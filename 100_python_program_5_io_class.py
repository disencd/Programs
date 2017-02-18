'''
Program : 100_python_program_5_io_class
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

'''

class IOclass:
    def __init__(self):
        self.string = ""

    def getstring(self):
        self.string = raw_input("Enter the string : ")

    def printstring(self):
        print (self.string.upper())

obj = IOclass()
obj.getstring()
obj.printstring()
