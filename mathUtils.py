import re, sys
import numpy as np


def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i


def historic(n):
    primes = set([2])
    i, p = 2, 0
    while True:
        if prime(i, primes):
            p += 1
            if p == n:
                return primes
        i += 1


def is_prime(n):
    """
    Returns True if n is prime, otherwise False.
    """
    return re.match(r'^1?$|^(11+?)\1+$', '1' * n) == None


def first_n_primes(n, min=0, max=100):
    """
    Returns n primes between min and max
    :param n: number of primes to return
    :param max: upperbound of search space. Default is 100
    :return: list of n primes
    """
    N = n                # number of primes
    M = max              # upper-bound of search space
    l = list()           # result list

    while len(l) < N:
        l += filter(is_prime, range(min, M)) # append prime element of [M - 100, M] to l
        M += 100                                # increment upper-bound

    return l[:N] # print result list limited to N elements


if __name__ == '__main__':
    print('mathUtils.py debug...')
    print(first_n_primes(3*8+1, 0, 100))
