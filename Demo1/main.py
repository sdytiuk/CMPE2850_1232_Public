# This is a sample Python script.
import datetime
"""
hello
I can type a whole block
"""

print("hello world", end="")

lyric = 'Hello class, it''s warmer out now'
print(lyric,lyric,lyric)

print(f'Today is {datetime.datetime.today().strftime("%Y-%m-%d %H.%M.%S")}')

help(datetime.datetime.today)

varGlobal = "snow"


def fncA():
    global varGlobal  # without this, varGlobal sent to shadows
    varGlobal = "rain"
    varfncA = "Anthony Henday"
    print('fncA : ', varGlobal)
    print('fncA: ',varfncA)

    def fncB():
        # global varfncA
        varfncA = "Whitemud Dr"
        print('fncB varGlobal: ', varGlobal)
        print('fncB fncA:', varfncA)

    fncB()
    print('fncA again: ', varfncA)


print('global: ', varGlobal)
fncA()
print('global2: ', varGlobal)
# print('fncAVar: ', varfncA)

import math

c = math.sqrt(3**2+4**2)
print(c)
c = math.sqrt(5**2+6**2)
print(c)

# range
for val in range(10):
    print('*',end="")
print()

# get the hypotenuses of all triangles size 1 to 10 (1,2; 3,4, etc)
for val in range(1,1000):
    c=math.sqrt(val**2+(val+1)**2)
    print(f"{val},{val+1}: {c}")

import random

max = random.randint(15, 25)
rnd = random.randint(0, max)

print(f"0 <= {rnd} <= {max}")