#!/usr/bin/python3

a = (input("Input a:"))
b = (input("Input b:"))
c = (input("Input c:"))

numbers = [a, b, c]

biggestval = numbers[0]

for val in (a,b,c):
    if val > biggestval:
        biggestval = val

print(f"The biggest value is: {biggestval}")
