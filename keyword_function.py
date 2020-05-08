#! /usr/bin/env python3

def keyword_function(a=1,b=2):
    return a+b
print(keyword_function(b=4,a=5))

print(keyword_function())  #it will use the default value

