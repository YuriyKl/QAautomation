#!/usr/bin/python3

sstring = "aab qq c badcc a qqqqqaqqqqaa tpara"

newstr = sstring.split()

s = [j.title() for j in newstr if j.count("a") == 2]
print(" ".join(str(e) for e in s))

# better code will be
# s = [j for j in sstring.split() if j.count("a") == 2]
# print(" ".join(s).title())