"""
Ближайший ноль

Временная сложность O(N)
Пространственная сложность O(N)

Решение в контесте: https://contest.yandex.ru/contest/22450/run-report/85015265/
"""
import sys


def main() -> None:
    array_length = int(input())
    array: list[str] = sys.stdin.readline().rstrip().split()

    zero_index = array_length - 1
    back_index = -1

    # Проходим по массиву только 1 раз слева направо
    for i in range(array_length):

        if array[i] != '0':
            # Если элемент не 0, то вычисляем дельту между его индексом и индексом прошлого нуля
            delta = abs(i - zero_index)
            array[i] = str(delta)
            continue

        # Если элемент -- это 0, то нужно обновить значения элементов, что слева от нового нуля.
        # Для этого итерируемся в обратную сторону: Стартуем от предыдущего элемента (i - 1) и движемся обратно
        # до тех пор, пока не дойдём до элемента более ближнего к прошлому нулю, чем к новому.
        # Либо пока не упрёмся в начало массива.
        for j in range(i - 1, back_index, -1):
            delta = abs(j - i)
            if int(array[j]) > delta:
                array[j] = str(delta)
            else:
                # Здесь мы находим либо первый элемент массива, либо более ближний элемент к левому нулю,
                # по этому завершаем цикл
                break

        zero_index = back_index = i

    print(' '.join(array))


if __name__ == '__main__':
    main()
