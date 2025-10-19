# from os import * # bad code
# from asyncio import *
# assert wait # you never know whether wait is part of os or asyncio

# better is 
# from os import path
# from asyncio import wait

# assert wait

#best will be
import os
import asyncio

assert asyncio.wait
assert os.path


# same problem with function args kwargs
def spam(eggs, *args, **kwargs):
    for arg in args:
        eggs += arg
    
    for extra_egg in kwargs.get('extra_eggs', []):
        eggs += extra_egg
    return eggs

print(spam(1, 2, 3, extra_eggs=[4, 5]))

# a resonable function name can help 
def sum_ints(*args):
    total = 0
    for arg in args:
        total +=arg
    return total

print(sum_ints(1, 2, 3, 4, 5))