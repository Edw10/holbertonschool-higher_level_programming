#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i + 1, 10):
        if i is not 8:
            print("{:d}{:d}, ".format(i, j), end='')
print("89")
