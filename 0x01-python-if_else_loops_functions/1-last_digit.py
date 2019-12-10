#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ognum = number
if number < 0:
    number = (-number) % 10
    number = -number
else:
    number = number % 10
if number == 0:
    print("Last digit of {:d} is {:d} and is 0".format(ognum, number))
elif number > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(ognum, number))
elif number < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0".format(ognum, number))
