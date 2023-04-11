#!/usr/bin/python3

sstring = "aab qq c badcc a qqqqqaqqqqaa tpara"

s=[i for i in sstring if i.count==2]
print(s)
newstr = sstring.strip()

type(newstr)

s=[i for j in newstr if j.count==2]
print(s)

# print(sstring.find("aa"))
# sind = sstring.rfind('aa')
print(sstring.split())

for i in newstr:
    print(i)
# print(sstring.find("aa"))
#
# for w in range(len(sstring)):
#     if w == sstring.find("aa"):
#         print(w)
# # print([x for x in sstring if newstr.find('aa')])

# print(sstring.count("aa"))
# for i in range(len(sstring)):
#     if sstring.count("a") == 2:
#         print(i)
# #     print(len(i))

# for i in sstring:
#     print(i.count("aa"))
# somestr =[el for el in multi_string if el.startswith(multi_string.)]
# sstring =multi_string.find(multi_string.capitalize(),multi_string.endswith("."))
# for i in sstring:
#     print(i)

# count = [i for i in multi_string if i.istitle() and i.endswith(".")]

# print(count)
