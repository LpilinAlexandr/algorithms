down_length = int(input())
right_length = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(down_length)]

y = int(input())
x = int(input())


left, right, top, bot = None, None, None, None

if right_length > 1:
    if x == right_length - 1:
        left = matrix[y][x - 1]
    elif x == 0:
        right = matrix[y][x + 1]
    else:
        left = matrix[y][x - 1]
        right = matrix[y][x + 1]

if down_length > 1:
    if y == down_length - 1:
        top = matrix[y - 1][x]
    elif y == 0:
        bot = matrix[y + 1][x]
    else:
        top = matrix[y - 1][x]
        bot = matrix[y + 1][x]

result = sorted([i for i in (left, right, top, bot) if i is not None])

print(' '.join(str(v) for v in result))
