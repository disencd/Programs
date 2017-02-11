#Distance calculating program using Oops

import math

class Point:
        def __init__(self, x = 0, y = 0): 
                self.move(x, y)

        def move(self, x, y): 
                self.x = x 
                self.y = y 

        def reset(self):
                self.x = 0 
                self.y = 0 

        def calculate_distance(self, other_point):
                # (x2 - x1) ^ 2 + (y2 - y1) ^ 2 
                return math.sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2)) 

a = Point()
print("x = " , a.x, " y = ", a.y)
a.move(5, 5)

print("x = " , a.x, " y = ", a.y)

b = Point(10,10)
dist = a.calculate_distance(b)
print("dist = " , dist)

a.reset()
b.reset()
