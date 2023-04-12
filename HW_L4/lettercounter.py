#!/usr/bin/python3

multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."

nstr=str(multi_string.split())
# print(len(multi_string.strip().split()))
print(nstr)
print(len(nstr))
for i in nstr:
    if i == i.startswith(nstr[0]) or i == i.startswith(".") and i.endwith("."):
        print(i)
        print(len([i]))
