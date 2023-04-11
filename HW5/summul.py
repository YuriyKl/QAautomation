#!/usr/bin/python3

MIN = 3
MAX = 6

lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]

sumlst =sum ([i for i in lst if i>=MIN or i<=MAX])

print(sumlst)


