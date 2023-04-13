#!/usr/bin/python3

sstring = "aab qq c badcc a qqqqqaqqqqaa tpara"

newstr = sstring.split()
print(newstr)
s=[j.title() for j in newstr if j.count("a")==2]
print(s)
