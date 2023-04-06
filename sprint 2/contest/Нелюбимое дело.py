# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item

        def __repr__(self):
            return f'{self.value}'


def solution(node, idx):
    """Удаляет из связного списка 1 элемент по индексу idx."""

    if idx == 0:
        return node.next_item

    i = 1
    temp = node

    while idx > i:
        temp = temp.next_item
        i += 1

    temp.next_item = temp.next_item.next_item
    return node



def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
