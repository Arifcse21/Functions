#! /usr/bin/env python3

def many(*args,**kwargs):
    print(args)
    print(kwargs)

many(1,2,3,name='mike',job='programmer')

