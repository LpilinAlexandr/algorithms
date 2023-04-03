"""
Ловкость рук

Временная сложность O(1)
Пространственная сложность O(1)

Решение в контесте: https://contest.yandex.ru/contest/22450/run-report/85031480/
"""
import sys
from collections import defaultdict


def main() -> None:
    numbers = defaultdict(int)
    k = 2 * int(input())

    for _ in range(4):
        layer = sys.stdin.readline().rstrip()
        for sign in layer:
            if sign.isdigit():
                numbers[sign] += 1

    win_count = sum(k >= i for i in numbers.values())

    print(win_count)


if __name__ == '__main__':
    main()
