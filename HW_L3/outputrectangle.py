#!/usr/bin/python3

height = int(input("Enter height of rectangular:"))
width = int(input("Enter width of rectangular: "))
symbol = (input("Enter symbol to build rectangular with: "))

for i in range(height):
    print(width*symbol)


