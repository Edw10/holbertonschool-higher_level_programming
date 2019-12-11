#!/usr/bin/python3
for i in range(122, 96, -1):

    a = i
    if (i % 2 != 0):
        a = i - 32
    print("{:c}".format(a), end='')
