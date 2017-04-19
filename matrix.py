'''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

class '''
Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''

class matrix_class(object):
    def __init__(self):
        self._mat_list = list()

    def _getRawCol(self):
        self._raw_col = raw_input('Enter the raw and col : ').split(',')
        
    def _printMatrix(self):
        self._mat_list = [[i * j  for j in range(int(self._raw_col[1]))] for i in range(int(self._raw_col[0]))]
        return self._mat_list

strObj = matrix_class()
strObj._getRawCol()
matr = strObj._printMatrix()
print matr(object):
    def __init__(self):
        self._mat_list = list()

    def _getRawCol(self):
        self._raw_col = raw_input('Enter the raw and col : ').split(',')
        
    def _printMatrix(self):
        self._mat_list = [[i * j  for j in range(int(self._raw_col[1]))] for i in range(int(self._raw_col[0]))]
        return self._mat_list

strObj = matrix_class()
strObj._getRawCol()
matr = strObj._printMatrix()
print matr
