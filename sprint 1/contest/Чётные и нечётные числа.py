import sys


def check(i):
    return int(i) % 2 == 0


a, b, c = [check(i) for i in sys.stdin.readline().rstrip().split()]

print("WIN" if a == b == c else "FAIL")
