#Name: Mengsang Korn
#Assignment 7
#CSCI 2001
#Python program: Rectangle class contains objects; width & height (private)
#.....................................and methods; getArea & getPerimeter.

class Rectangle:
    def __init__(self, width = 1, height = 2):  #initialize rectangle objects
        self.__width  = width
        self.__height = height

    def getWidth(self):
        return self.__width                     #private width

    def getHeight(self):
        return self.__height                    #private height

    def getArea(self):                          #return area of rectangle
        return self.__width * self.__height

    def getPerimeter(self):                     #return perimeter of rectangle
        return 2*(self.__width + self.__height)

def main():
    rec1 = Rectangle(4,40)                      #a 4 by 40 rectangle
    print("A",rec1.getWidth(),"x", rec1.getHeight(),"rectangle has an area of",
          rec1.getArea(), "and a perimeter of", rec1.getPerimeter(),'\b.')

    rec2 = Rectangle(3.5, 35.7)                 # a 3.5 by 35.7 rectangle
    print("A", rec2.getWidth(), "x", rec2.getHeight(),
          "rectangle has an area of", format(rec2.getArea(),".2f"),
          "and a perimeter of", format(rec2.getPerimeter(),".2f"),'\b.')

main()                                          #Call the main function



'''******************************-out-put-*************************************

A 4 x 40 rectangle has an area of 160 and a perimeter of 88.
A 3.5 x 35.7 rectangle has an area of 124.95 and a perimeter of 78.40.

*****************************************************************************'''





