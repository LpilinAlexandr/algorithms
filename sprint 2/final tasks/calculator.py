"""
-- ПРИНЦИП РАБОТЫ --
Ссылка на прохождение в contest: https://contest.yandex.ru/contest/22781/run-report/85512155/

Реализован алгоритм вычисления выражения, записанного в обратной польской нотации.
Алгоритм итерируется по массиву. Проверяет каждый следующий элемент - это оператор или операнд.
Если элемент - это операнд, то он кладётся в стек.
Если элемент - оператор, то из стека достаётся два последних операнда таким образом,
что последний оказывается справа от оператора, а предпоследний слева.
После происходит вычисление над операндами при помощи eval. Результат также кладётся в стек.
Таким образом алгоритм доходит до конца массива, а после возвращает первый элемент из стека.
Оператор "/" меняется на "//", т.к. в Python это оператор целочисленного деления.


-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
В Худшем случае каждый операнд инициирует одно действие - положить елемент в стек.
А каждый оператор 4 действия - достать из стека 2 элемента, сложить их и положить резальтат в стек
Количество действий константно. Константу отбрасываем. И т.к. алгоритм итерируется по массиву 1 раз, то
временная сложность алгоритма будет O(N)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В худшем случае, если в массиве будут только операторы, то они все окажутся в стеке.
Таким образом амортизационная пространственная сложность O(N)
"""


if __name__ == '__main__':
    array = input().split()

    result = None
    stack = []

    for sign in array:

        if sign == '/':
            sign = '//'

        if sign[-1].isdigit():
            stack.append(sign)
            continue

        b = stack.pop()
        a = stack.pop()

        res = eval(f'{a} {sign} {b}')

        stack.append(res)

    result = stack.pop()

    print(result)
