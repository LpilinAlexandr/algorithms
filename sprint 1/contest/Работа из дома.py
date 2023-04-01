number = int(input())

result = ''

while number > 1:
    if number % 2 == 0:
        result = f'0{result}'
    else:
        result = f'1{result}'

    number = number // 2

print(f'{number}{result}')
