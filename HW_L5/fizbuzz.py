#!/usr/bin/python3
# Solution 1
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
fizz = [f for f in lst if f% 3 == 0 and f %5!=0]
buzz = [b for b in lst if b% 5 == 0 and b %3!=0]
fizzbuzz = [fb for fb in lst if fb% 3 == 0 and fb% 5 == 0]
print(fizz)
print(buzz)
print(fizzbuzz)
