#!/usr/bin/python3
import sys
def factorize_number(n):
    """"find two small numbers that multiply to give a given number"""
    i =2
    if n < 2:
        return
    while n % i:
        i++
    print("{:.0f}={:.0f}*{:.0f}".format(n, n / i, i))

    if len(argv) != 2:
        exit()
    try:
        with open(argv[1]) as file:
            line = file.readline()

            while line != "":
                n = int(line.split('\n')[0])
                factorize_number(n)
                line = file.readline()
    except:
        pass
