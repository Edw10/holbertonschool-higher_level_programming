#!/usr/bin/python3
print("00", end='')
for i in range(0, 10):
    for j in range(i + 1, 10):
        print(", {:d}{:d}".format(i, j), end='')
print("")
