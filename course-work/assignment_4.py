#Name: Mengsang Korn
#Assignment 4
#Class: CSCI 2001
#Python program: solves quadratic equations

import math

#promt user for inputs
a, b, c = eval(input("Enter a, b, c: "))

#solve for discriminant
discriminant = pow(b,2) - (4*a*c)

#infinite solutions if 'a','b',and 'c' are all '0'
if (a == b == c ==0):
    print("There are infinite solutions")
#no solution if 'a' and 'b' are '0', but 'c' is not '0'
elif (a == b == 0) and (c != 0):
    print("There is no solution!")
#only one solution if 'a' is '0', but 'b' is not '0'
elif (a == 0) and (b != 0):
    x1 = (-c)/b
    print("The root is", format(x1,".2f"))
#avoid square root of negative number
elif discriminant < 0:
    print("There is no solution since discriminant is negative")
#only one real solution when discriminant is '0'
elif discriminant == 0:
    x2 = (-b -math.sqrt(discriminant)) /(2*a)
    print("The root is", format(x2,".2f"))
else:
    #solve for x(s)
    x3  = (-b +math.sqrt(discriminant)) /(2*a)
    x4 = (-b -math.sqrt(discriminant)) /(2*a)
    print("The roots are", format(x3,".2f"), "and", format(x4,".2f"))


'''***********************************out-put***********************************
Enter a, b, c: 1.0, -1.0, -6.0
The roots are 3.00 and -2.00

Enter a, b, c: 1.0, -15.0, 0.0
The roots are 15.00 and 0.00

Enter a, b, c: 1.0, 0.0, -16.0
The roots are 4.00 and -4.00

Enter a, b, c: 3.0, 3.0, -6.0
The roots are 1.00 and -2.00

Enter a, b, c: 1.0, 2.0, 1.0
The root is -1.00

Enter a, b, c: 0.0, 6.0, 3.0
The root is -0.50

Enter a, b, c: 1.0, -6.0, 13.0
There is no solution since discriminant is negative

'''






