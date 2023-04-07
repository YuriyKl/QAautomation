#!/usr/bin/python3


check_palindrom = str(input("Please, enter any string for the palindrome check:"))

lowstr = check_palindrom.lower().split()
print("This string is palindrome" if lowstr == lowstr[::-1] else "This string is NOT palindrome")