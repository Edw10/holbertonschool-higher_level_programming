#!/usr/bin/python3
def print_last_number(number):
    if number < 0:
        number = -number
    number = number % 10
    print("{:d}".format(number))
    return number
