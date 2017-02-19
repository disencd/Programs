"""
Program : 100_python_program_7_list_program
Question:
"""
inp = raw_input("Enter row and column :").split(",")

row = int(inp[0])
column = int(inp[1])
print (row, column)

matrix = [[0  for r in range(row)] for c in range(column)]
for r in range(row):
    for c in range(column):
        matrix[r][c] = r*c

print matrix

