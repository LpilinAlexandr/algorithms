numbers = [
    input()[::-1],
    input()[::-1]
]

flag = False
result_list = []

long = numbers.pop(0) if len(numbers[0]) > len(numbers[1]) else numbers.pop(-1)
short = numbers[0]

storage = {
    0: '0',
    1: '1',
    2: '10',
    3: '11'
}

for i in range(len(long)):

    long_num = int(long[i])
    short_num = int(short[i]) if i < len(short) else None

    if short_num is not None:
        if flag:
            flag = False
            numbers = long_num + short_num + 1
        else:
            numbers = long_num + short_num
    else:
        if flag:
            flag = False
            numbers = long_num + 1
        else:
            result_list.insert(0, ''.join(long[i:])[::-1])
            break

    result = storage[numbers]

    if result == storage[2] or result == storage[3]:
        flag = True

    result = result[-1]
    result_list.insert(0, result)

if flag:
    result_list.insert(0, '1')

print(''.join(result_list))
