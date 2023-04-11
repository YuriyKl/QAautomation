#!/usr/bin/python3

multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
nstr=multi_string.split()
# for i in nstr:
#     print(i)
#     print(len(i))

somestr =[el for el in multi_string if el.endswith(".")]
print(somestr)
# sstring =multi_string.find(multi_string.capitalize(),multi_string.endswith("."))
# for i in sstring:
#     print(i)

# count = [i for i in multi_string if i.istitle() and i.endswith(".")]

# print(count)