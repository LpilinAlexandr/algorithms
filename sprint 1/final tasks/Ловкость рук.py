"""
Ловкость рук

Временная сложность O(N)
Пространственная сложность O(N)
"""
import sys
from collections import defaultdict

win_count = 0
numbers = defaultdict(int)

k = 2 * int(input())

for _ in range(4):
    layer = sys.stdin.readline().rstrip()
    for sign in layer:
        if sign.isdigit():
            numbers[sign] += 1

for i in numbers.values():
    if k >= i:
        win_count += 1

print(win_count)
