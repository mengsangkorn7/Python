# Name: Mengsang Korn
# Assignment 9
# CSCI 2001
# Python program: assign grade


def getScores():                        # get scores from user
    lst = []                            # empty list for storing scores
    score = int(input("Enter scores or -999 to finish: "))
    while score != -999:                # sentinel value to end loop is -999
        lst.append(score)  # append/put score into list every time loop ran
        score = int(input("Enter scores or -999 to finish: "))
    return lst                          # return a list of scores


def printGrade(scores):                 # display grade for each scores in the list
    best = 100                          # use 100 for best score
    for score in scores:                # go through every score in the list
        if score >= (best-10):          # grade A if score >= 90
            print(score, "is an A")
        elif score >= (best-20):        # grade B if 90 > score >= 80
            print(score, "is a B")
        elif score >= (best-30):        # grade C if 80 > score >= 70
            print(score, "is a C")
        elif score >= (best-40):        # grade D if 70 > score >= 60
            print(score, "is a D")
        else:                           # grade F if score < 60
            print(score, "is an F")


def main():
    scores = getScores()                # call getScores() func.
    printGrade(scores)                  # call printGrade() func.


main()                                  # call the main function


'''***********************************out-put***********************************

Enter scores or -999 to finish: 94
Enter scores or -999 to finish: 83
Enter scores or -999 to finish: 72
Enter scores or -999 to finish: 61
Enter scores or -999 to finish: 59
Enter scores or -999 to finish: -999
94 is an A
83 is a B
72 is a C
61 is a D
59 is an F

'''
