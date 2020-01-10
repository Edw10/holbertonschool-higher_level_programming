#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    for i in range(0, x):
        try:
            a = a + 1
            print("{:d}".format(my_list[i]), end='')
        except:
            a = a - 1
    print()
    return a
