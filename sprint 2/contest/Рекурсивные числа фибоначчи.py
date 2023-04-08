

def fibonacci_recursively(n, a=0, b=1):

    if not n:
        return b

    return fibonacci_recursively(n-1, b, a + b)
