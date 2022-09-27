"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

import math

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError()


    list = []
    counter = 1;
    while len(list) < number_of_primes:
        isPrime = True
        counter += 1
        for i in range(2, int(math.sqrt(counter)) + 1):
            if(counter % i == 0):
                isPrime = False
        if isPrime:
            list.append(counter)

            
    return list
