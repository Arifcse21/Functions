#! /usr/bin/env python3
def mixed_fun(a,b=2,c=3):
    return a+b+c
#print(mixed_fun(b=4,c=5)) # it needs the value of a cause a doesn't have default Value
print(mixed_fun(1,b=4,c=5))
print(mixed_fun(1)) # it wil use the other default values




