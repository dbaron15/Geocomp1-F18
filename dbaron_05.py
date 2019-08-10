# Deana Baron
# GTECH731
#
# Assignment 5: creating a class and object for lines

import math

class Line(object):
    def __init__(self, x1, y1, x2, y2): #default __init__ function, takes the inputted coordinates of the line, converts to float
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)

    def convertPoints(self): # converts individual coords into point lists
        p1 = (self.x1, self.y1)
        p2 = (self.x2, self.y2)
        return p1, p2

    def length (self): #calculates the length of the line using pythagorean theorum
        dx = abs(self.x1 - self.x2) #distance between x
        dy = abs(self.y1 - self.y2) #distance between y
        sq_dx = dx ** 2 #x distance squared
        sq_dy = dy ** 2 #y distance squared
        length = math.sqrt(sq_dx + sq_dy) #square root of the squared x distance plus squared y distance
        return length

    def slope (self): #calculates the slope of the line
        dx = self.x1 - self.x2 #distance between x
        dy = self.y1 - self.y2 #distance between y
        slope = dy / dx #slope = distance of y over distance of x
        return slope

#Let's test the class

#create points
x1 = 2
y1 = 4
x2 = 10
y2 = 14

#convert to a line
line = Line(x1, y1, x2, y2)

#convert to points
line2 = line.convertPoints()

#Display the line
print(line2)

#calculate the length
line_length = line.length()
print (line_length)

#calculate the slope
line_slope = line.slope()
print (line_slope)

