from functools import lru_cache

# lru_cache() is one such function in functools module which helps in
# reducing the execution time of the function by using memoization technique
# Least Recently Used cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check that input is a positive integer
    if type(n) != int:
        raise TypeError('n must be a positive int')
    if n < 1:
        raise ValueError('n must be a positive int')
    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    return value

for n in range(1,1001):
    print(n,fibonacci(n))