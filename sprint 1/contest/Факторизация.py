number = int(input())

res = []

i = 2

while i <= number:

    if number % i == 0:
        number /= i
        res.append(str(i))
    else:
        if i * i > number:
            # Если i > чем квадратный корень числа number, то это значит,
            # что большего делителя мы уже не найдём, т.к. число number -- простое.
            # Корень ищем при помощи умножения. Потому что операция вычисления корня дороже умножения
            res.append(str(int(number)))
            break
        else:
            i += 1

print(' '.join(res))
