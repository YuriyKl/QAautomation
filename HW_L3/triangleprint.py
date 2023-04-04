#!/usr/bin/python3

size = int(input("Enter size of triangle: "))

rangesize = range(size)

for i in reversed(rangesize):
       for j in range(size):
              if j<i:
                     print(" ", end="")
              else:
                     print("*", end="")
       print()
