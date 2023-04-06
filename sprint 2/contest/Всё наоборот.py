# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class DoubleConnectedNode:
        def __repr__(self):
            return f'{self.value}'

        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev


def solution(node):
    """Разворачивает 2-связный список."""
    temp = node.next
    new_node = None

    while temp:
        new_node = temp
        temp = temp.next

        new_node.next = node
        node.next = node.prev
        node.prev = new_node

        node = new_node

    if new_node:
        new_node.prev = None
        return new_node

    node.next, node.prev = node.prev, node.next
    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1


if __name__ == '__main__':
    test()
