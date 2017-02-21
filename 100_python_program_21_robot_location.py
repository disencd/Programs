'''

Programs:100_python_program_21_robot_location.py
Question 21

A robot moves in a plane starting from the original point (0,0) The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
Example
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
import math
steps = [0, 0]
while(1):
    inp = raw_input("dir< >pos    :")

    if not inp:
        break

    else:
        input = inp.split(" ")
        dir = input[0]
        pos = input[1]

        if dir == "UP":
            steps[1] += int(pos)
            print("UP Number of Steps " , steps)

        elif dir == "DOWN":
            steps[1] -= int(pos)
            print("DOWN Number of Steps " , steps)

        elif dir == "RIGHT":
            steps[0] += int(pos)
            print("RIGHT Number of Steps " , steps)

        elif dir == "LEFT":
            steps[0] -= int(pos)
            print("LEFT Number of Steps " , steps)

        else:
            break

print("Position " , steps)

dist = round(math.sqrt(steps[0] ** 2 + steps[1] ** 2))

print("Distance from origin " , dist)
