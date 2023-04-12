#!/usr/bin/python3

sstring = "aab qq c badcc a qqqqqaqqqqaa tpara"


s=[j.title() for j in sstring if j.count("a")==2]
print(s)
