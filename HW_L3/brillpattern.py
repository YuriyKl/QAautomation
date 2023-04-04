#!/usr/bin/python3

min_width = int((input("Enter minimal width: ")))
max_width = int((input("Enter maximal width: ")))

while True:
    if min_width > max_width:
        print("Minimal width can not be greater than Maximal width")
        quit()
    elif (max_width-min_width)%2 == 1:
        print("The difference between the maximum width and the minimum width must be a multiple of 2")
        quit()
    else:
        print(min_width*"*")
        print("*"*max_width[-1] and "*"*max_width)
        break


