quantity = int(input())

array = [int(i) for i in input().split()]

count = 0

for i in range(quantity):

    is_first = i == 0
    is_last = i == quantity - 1

    if is_last and is_first:
        count += 1
    elif is_first and array[i] > array[i + 1]:
        count += 1
    elif is_last and array[i] > array[i - 1]:
        count += 1
    elif array[i - 1] < array[i] > array[i + 1]:
        count += 1

print(count)
