#Name: Mengsang Korn
#Assignment 6
#CSCI 2001
#Python program: return the Area and Perimeter of a rectangle...
#               ...using customized functions; 'getArea' and 'getPerimeter'

#define getArea function
def getArea(w, h):
    return w * h            #Area of a rectangle = width * height

#define getPerimeter function
def getPerimeter(w, h):
    return 2* (w+h)         #Perimater of a rectangle = 2*(width+height)


def main():
    #prompt user for inputs
    width  = eval(input("Enter value for width of a rectangle: "))
    height = eval(input("Enter value for height of a rectangle: "))

    area = getArea(width, height)               #call getArea function
    perimeter = getPerimeter(width, height)     #call getPerimeter function

    #display output
    print("The area is: ", format(area,".2f"))
    print("The perimeter is: ", format(perimeter,".2f"))

main()      #call the main function





'''***********************************out-put***********************************
Test #1:
Enter value for width of a rectangle: 4
Enter value for height of a rectangle: 40
The area is:  160.00
The perimeter is:  88.00

Test #2:
Enter value for width of a rectangle: 3.5
Enter value for height of a rectangle: 35.7
The area is:  124.95
The perimeter is:  78.40


'''
