#!/usr/bin/python3

rows = int(input("Enter quantity of rows of triangle: "))
base = (2*rows)-2
# base = (2*rows)-2

for i in range(1, rows+1):
       for j in range(1,base+1):
              print(end=" ")
       base -= 1
       for j in range(0, i):
              print(i, end=" ")
       print(" ")