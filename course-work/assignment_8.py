# Name: Mengsang Korn
# Assignment 8
# CSCI 2001
# Python program: check password


def getPW():                # prompt user for password
    return input("Please enter a password: ")


def isValidPW(pw):          # check if the password is valid
    boolean = True          # default password to valid

    if len(pw) < 8:         # invalid if less than 8 characters in pw
        print("Password must be at least 8 characters long.")
        boolean = False
    if not pw.isalnum():    # invalid if pw aren't all alphanumeric
        print("Password must be alphanumeric.")
        boolean = False

    digits = 0              # count number of digits in pw
    for i in pw:
        if i.isdigit():
            digits += 1
    if digits < 2:          # invalid if pw has less than 2 digits
        print("Password must have at least 2 digits.")
        boolean = False
    return boolean


def main():
    pw = getPW()            # get password from user

    if not isValidPW(pw):   # check if the password is valid/True
        print(pw, "is invalid")
    else:
        print(pw, "is valid")


main()                      # call the main function
















'''***********************************out-put***********************************
Please enter a password: abcd1234
abcd1234 is valid.

Please enter a password: abcd123
Password must be at least 8 characters long.
abcd123 is invalid.

Please enter a password: abcdefg8
Password must have at least 2 digits.
abcdefg8 is invalid.

Please enter a password: abcd123*
Password must be alphanumeric.
abcd123* is invalid.

Please enter a password: abc3*
Password must be at least 8 characters long.
Password must be alphanumeric.
Password must have at least 2 digits.
abc3* is invalid.

'''
