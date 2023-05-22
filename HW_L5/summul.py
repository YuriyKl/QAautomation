#!/usr/bin/python3
import math

MIN = 3
MAX = 6

lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
sumlst =sum(i for i in lst if i>=MIN if i<=MAX)
multlst = math.prod(i for i in lst if i>=MIN if i<=MAX)
print(sumlst)
print(multlst)


