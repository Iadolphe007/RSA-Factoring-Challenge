#!/usr/bin/python3
import sys


def factorize(num):
    """ Generate 2 factors for a given number"""
    num1 = 2
    while (num % num1):
        if (num1 <= num):
            num1 += 1
    num2 = num // num1
    return (num2, num1)

    if len(sys.argv) != 2:
        sys.exit(f"Wrong usage: {sys.argv[0]} <file_path>")

    file_name = sys.argv[1]
    file = open(file_name, 'r')
    lines = file.readlines()

    for line in lines:
        num = int(line.rstrip())
        num2, num1 = factorize_num(num)
        print(f"{num} = {num2} * {num1}")
