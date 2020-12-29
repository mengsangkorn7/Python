#Name: Mengsang Korn
#Assignment 5
#CSCI 2001
#Python program: Count positive and negative numbers...
#               ...and compute the average of numbers

sum = 0             #initialized sum/total to '0'
count = 0           #for how many time while loop has run
posNum = 0          #number of positives
negNum = 0          #number of negatives

# prompt user for input
number = eval(input("Enter an integer, the input ends if it is 0: "))
while number != 0:          #while loop ends if input is '0'
    count += 1              #update counter
    sum += number           #increment sum with input value
    if number < 0:
        negNum += 1         #increment #of negatives if input < 0
    elif number > 0:
        posNum += 1         #increment #of positives if input > 0
    else:
        pass
    number = eval(input("Enter an integer, the input ends if it is 0: "))

if sum == 0:
    #display message error
    print("You didn't enter any number")
else:
    #only calculate average and display the output if there's input
    average = sum / (count)
    print("The number of positives is ", posNum)
    print("The number of negatives is ", negNum)
    print("The total is ", sum)
    print("The average is ", format(average, ".2f"))



'''***********************************out-put***********************************
Test #1:
Enter an integer, the input ends if it is 0: 1
Enter an integer, the input ends if it is 0: 2
Enter an integer, the input ends if it is 0: -1
Enter an integer, the input ends if it is 0: 3
Enter an integer, the input ends if it is 0: 0
The number of positives is  3
The number of negatives is  1
The total is  5
The average is  1.25

Test #2:
Enter an integer, the input ends if it is 0: 0
You didn't enter any number

'''






