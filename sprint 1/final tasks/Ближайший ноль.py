
array = [0, 7, 9, 4, 8, 20, 2]
array_length = len(array)
result = [array_length - 1] * array_length


def go(parent_array: list, result_array: list, invert: bool = False):
    zero_index = len(parent_array) - 1 if not invert else 0

    iterator = range(len(parent_array)) if not invert else range(len(parent_array) - 1, -1, -1)

    for i in iterator:

        if parent_array[i] == 0:
            zero_index = i
            result_array[i] = 0
            continue

        delta = abs(i - zero_index)
        if result_array[i] > delta:
            result_array[i] = delta

    return result_array


result = go(array, result_array=result)
result = go(result, result_array=result, invert=True)

print(' '.join(str(i) for i in result))
