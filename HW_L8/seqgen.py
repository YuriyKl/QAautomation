#!/usr/bin/python3
# solution 1
def generator(pows, nums):
    for _pow in range(1,pows+1):
        for num in range(1,nums+1):
            yield pow(num,_pow)

# solution 2
def generator2(pows, nums):
    return (pow(num,_pow) for _pow in range(1,pows+1) for num in range(1,nums+1))
