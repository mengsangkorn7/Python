#Name: Mengsang Korn
#Assignment 3
#Class: CSCI 2001
#Python program: takes length from the center of a hexagon to vertex...
#...and computes/outputs the area

import math

#prompt user for the length
length = eval(input("Enter the length from the center to a vertex:"))

#compute the side using inputed length
side = 2 * length * math.sin(math.pi/6)

#calculate the area
area = ( (3*math.sqrt(3)) /2) *pow(side,2)

#print the output message and area
print("The area of the hexagon is ", format(area,".2f"))


'''*******************************out-put***************************************
Enter the length from the center to a vertex:5.5
The area of the hexagon is  78.59

Enter the length from the center to a vertex:100
The area of the hexagon is  25980.76

Enter the length from the center to a vertex:50.0
The area of the hexagon is  6495.19
'''