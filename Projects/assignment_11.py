# Name: Mengsang Korn
# Assignment 11
# CSCI 2001
# Python Program: Create 3x3 matrix and sum every element row by row
 

def get_matrix():                       # get 3x3 matrix
    matrix = []                         # Create an empty list
    number_of_row = 2
    number_of_col = 3
    print('Enter matrix elements row by row:')
    for row in range(number_of_row):    
        matrix.append([])               # Add an empty new row             
        for column in range(number_of_col):
            value = eval(input("Enter the next element: "))
            matrix[row].append(value)
    return matrix                       # return the matrix                      


def print_matrix(matrix):               # print matrix row by row
    for row in matrix:              
        for value in row:
            print(value, end="  ")
        print() # Print new line


def get_sum_row(matrix, row_index):    # get the sum of the element of single row
    for rows in range(0,row_index): 
        sumRow = 0
        for column in range(0, len(matrix[0])):  
            sumRow += matrix[rows][column] 
    return sumRow


def main():
    m = get_matrix()                    # Call get_matrix()
    print_matrix(m)                     # Call print_matrix()
   
    for row in range(1,3):
        total = get_sum_row(m, row)     # Call get_sum_row()
        print("The sum of row", row, "is", total)


main()                                  # call the main function










'''***********************************out-put***********************************

Enter matrix elements row by row:
Enter the next element: 1
Enter the next element: 2
Enter the next element: 3
Enter the next element: 4
Enter the next element: 5
Enter the next element: 6
Enter the next element: 7
Enter the next element: 8
Enter the next element: 9
1  2  3
4  5  6
7  8  9
The sum of row 1 is 6
The sum of row 2 is 15
The sum of row 3 is 24

'''
