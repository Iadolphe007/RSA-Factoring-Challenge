import math
import sys

def find_factors(number):
    factors []
    for i in range int(math.square(number) +1):
        if number % i == 0:
            factors.append((i, number // i))
    return factors
