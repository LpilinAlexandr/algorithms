
N = 1000000
K = 8


def fibonacci_module(n, k):

    a = 0
    b = 1
    coeff = 10 ** k

    while n:
        a, b = b % coeff, a + b
        n -= 1

    return b % coeff


print(fibonacci_module(N, K))

