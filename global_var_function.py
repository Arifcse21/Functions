#! /usr/bin/env python3

def function_1():
    global a
    a=1
    b=2
    return a+b
def function_2():
    c=3
    return a+c
print(function_1())
print(function_2())


