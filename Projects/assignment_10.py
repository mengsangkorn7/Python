# Name: Mengsang Korn
# Assignment 11
# CSCI 2001
# Python program: 


def get_matrix():
    matrix = []          #create an empty list

    number_of_row = 3
    number_of_col = 3

    print('Enter matrix elements row by row:')

    for row in range(number_of_row):
        matrix.append([])
        for collum in range(number_of_col):
            value = eval(input("Enter the next element: "))
            magrix[row].append(value)

    return  matrix[row][collum]


def print_matrix(m):
    print(m)


def main():
    m = get_matrix
    print_matrix(m)


main()                          # call the main function








'''***********************************out-put***********************************
'''
