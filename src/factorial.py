#!/bin/python3
'''
calculate the factorial of a number
'''

def factorial(num):

    output = 1

    for i in range(2,num+1):
        output = output * i

    return output

print(factorial(4))
