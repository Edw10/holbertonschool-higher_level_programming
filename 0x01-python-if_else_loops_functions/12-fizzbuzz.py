#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            if i % 5 == 0:
                print("fizzBuzz", end=" ")
            else:
                print("fizz", end=" ")
        elif i % 5 == 0:
            print("buzz", end=" ")
        else:
            print("{:d}".format(i), end=" ")
