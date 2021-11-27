from math import isqrt
def sieve(n):
    tablica = [True] * n
    tablica[0] = False
    tablica[1] = False

    for i in range(2,isqrt(n)):
        if tablica[i]:
            for j in range(i * i, n , i):
                tablica[j] = False

    primes = [ x for x in range(n) if tablica[x] == True ]

    return primes
