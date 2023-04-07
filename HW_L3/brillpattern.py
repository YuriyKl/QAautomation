#!/usr/bin/python3

min_width = int((input("Enter minimal width: ")))
max_width = int((input("Enter maximal width: ")))


if min_width > max_width:
    print("Minimal width can not be greater than Maximal width")
    quit()
elif (max_width-min_width)%2 == 1:
    print("The difference between the maximum width and the minimum width must be a multiple of 2")
    quit()
dif =(max_width-min_width)//2

for i in range(2*dif):
    print(i)
    for j in range(1,dif):
        print("", end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*"*min_width, end="")
        else:
            print("", end="")
    print()


    # if i==min_width or i==max_width:
    #     print("*" * i, end="")
    #
    # else:
    #     print("*" + ""*(i-2) + "*")
    #
