"""
-- ПРИНЦИП РАБОТЫ --
Ссылка на прохождение в contest: https://contest.yandex.ru/contest/22781/run-report/85461183/

Я реализовал Дек с использованием кольцевого буфера:
При инициализации Дека внутри задаётся массив фиксированной длины.
В каждом индексе массива лежит ссылка на один объект -- SpecialEmpty.
Это нужно для того, чтобы внутрь можно было класть любой Python объект, в том числе None.
Также мы фиксируем индекс начала (head), конца (tail) и размер (size) на нуле.

При добавлении в конец или в начало мы кладём элемент на соответствующий индекс.
В конец на индекс tail, а в начало на индекс head. В случае если индекс не свободен,
мы сначала сдвигаем его по направлению в другую сторону от противоположного.
Это нужно для того, чтобы голова и хвост расходились в разные стороны массива.

При удалении элемента из Дека мы заменяем элемент массива по соответствующему индексу на SpecialEmpty.
А также мы обрабатываем крайний случай - это когда происходит удаление последнего элемента.
В этот момент индексы head и tail равны и они не должны сдвигаться:

Все индексы сдвигаются закольцовано.

-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Пример Добавления элементов спереди и сзади:

deque = Deque(5)
deque = [SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty]

deque.push_back(123)
# Так как по индексу head и tail == 0 ничего нет, то элемент кладётся на этот индекс. Индексы head и tail не сдвигаются.
deque = [123, SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty]
         ^^^
    Здесь находится head и tail

deque.push_front('qwertry')
# Так как по индексу head уже находится какой-то элемент, то он сдвигается на head -= 1

deque = [123, SpecialEmpty, SpecialEmpty, SpecialEmpty, 'qwertry']
         ^^^                                               ^^^
        tail = 0                                          head = 4

deque.push_back(None)
# Так как по индексу tail уже что-то лежит, то мы сдвигаем индекс tail на tail += 1
deque = [123, None, SpecialEmpty, SpecialEmpty, 'qwertry']
              ^^^                                   ^^^
              tail = 1                              head = 4

По такому же принципу добавляются все остальные элементы, до тех пор пока в массиве не останется SpecialEmpty.
Теперь рассмотрим принцип удаления элемента из Дека:

deque.pop_back()
# Заменяем элемент None по индексу tail = 1 на SpecialEmpty и сдвигаем tail -= 1
deque = [123, SpecialEmpty, SpecialEmpty, SpecialEmpty, 'qwertry']
         ^^^                                               ^^^
        tail = 0                                         head = 4

deque.pop_back()
# Заменяем элемент 123 по индексу tail = 0 на SpecialEmpty и сдвигаем tail -= 1
deque = [SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty, 'qwertry']
                                                                  ^^^
                                                              tail = head = 4

deque.pop_front()
# Заменяем элемент 'qwertry' по индексу head = 4 на SpecialEmpty, но индексы не сдвигаем, т.к. они равны
deque = [SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty, SpecialEmpty]
                                                                  ^^^
                                                              tail = head = 4

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Для любой операции происходит константное кол-во действий, не зависящее от размера массива.
Таким образом можно считать временную сложность O(1)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Размер Дека константен и равен его максимальному размеру. Таким образом если максимальный размер равен N,
то потребление памяти будет O(N).
"""
import sys


class SpecialEmpty:
    """
    Специальный объект, который кладётся на пустое место в массиве Дека,
    чтобы туда можно было класть любой Python объект.
    """


class Deque:
    """
    Реализация структуры данных Deque, в котором все операции выполняются за O(1).

    Методы добавления и удаления похожи. Их можно оптимизировать, убрав дублирование кода.
    Но я решил оставить так. Т.к. так проще понять логику работы каждого метода в отдельности.
    """

    __EMPTY = SpecialEmpty()

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [self.__EMPTY] * max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_back(self, item):
        assert not isinstance(item, SpecialEmpty), 'SpecialEmpty нельзя положить в Deque'
        if self.size == self.max_size:
            raise IndexError('Кол-во элементов в Deque достигло максимума')

        if self.queue[self.tail] is not self.__EMPTY:
            self.tail = (self.tail + 1) % self.max_size

        self.queue[self.tail] = item
        self.size += 1

    def pop_back(self):
        item = self.queue[self.tail]
        if item is self.__EMPTY:
            raise IndexError('Deque пуст')

        self.queue[self.tail] = self.__EMPTY
        self.size -= 1
        if self.size:
            self.tail = (self.tail - 1) % self.max_size

        return item

    def push_front(self, item):
        assert not isinstance(item, SpecialEmpty), 'SpecialEmpty нельзя положить в Deque'
        if self.size == self.max_size:
            raise IndexError('Кол-во элементов в Deque достигло максимума')

        if self.queue[self.head] is not self.__EMPTY:
            self.head = (self.head - 1) % self.max_size

        self.queue[self.head] = item
        self.size += 1

    def pop_front(self):
        item = self.queue[self.head]
        if item is self.__EMPTY:
            raise IndexError('Deque пуст')

        self.queue[self.head] = self.__EMPTY
        self.size -= 1
        if self.size:
            self.head = (self.head + 1) % self.max_size

        return item


def main():
    """Основная функция с реализацией проверки структуры данных Deque."""
    commands_count = int(input())
    deque = Deque(int(input()))

    for i in range(commands_count):
        command, *arg = sys.stdin.readline().rstrip().split()

        try:
            print(getattr(deque, command)()) if not arg else getattr(deque, command)(int(arg[0]))
        except IndexError:
            print('error')


if __name__ == '__main__':
    main()
