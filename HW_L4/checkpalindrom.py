#!/usr/bin/python3


check_palindrom = str(input("Please, enter any string for the palindrome check:"))

# Solution 1
lowstr = check_palindrom.casefold().strip()
print("This string is palindrome" if lowstr == lowstr[::-1] else "This string is NOT palindrome")

# Solution 2
chkstr = check_palindrom.lower().strip()
revstr = reversed(chkstr)
print("This string is palindrome" if list(chkstr) == list(revstr) else "This string is NOT palindrome")
# print("This string is palindrome" if list(chkstr) == list(revstr) else "This string is NOT palindrome")
