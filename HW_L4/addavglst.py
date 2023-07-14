#!/usr/bin/python3

lst = [3.5, 2, 4, 6.2, 8]
lst2 =[]

for i in range(len(lst)):
    lst2.append(lst[i])
    if i<len(lst)-1:
        avg = (lst[i]+lst[i+1])/2
        lst2.append(avg)

print(lst2)