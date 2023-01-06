from adt.Node import Node


class Stack:
    def __init__(self):
        self.first = None
        self.n = 0
        self._cur_node = None
        self._cur_index = 0

    def push(self, item: object):
        old_first = self.first
        self.first = Node(item)
        self.first.next = old_first
        self.n += 1

    def pop(self) -> object:
        if self.size() == 0:
            return None
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        return item

    def is_empty(self) -> bool:
        return self.first is None

    def size(self):
        return self.n

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_node is None:
            if self.n != 0 and self._cur_index == 0:
                self._cur_node = self.first
                node = self._cur_node
                self._cur_node = self._cur_node.next
                self._cur_index += 1
            else:
                self._cur_index = 0
                raise StopIteration
        else:
            node = self._cur_node
            self._cur_node = self._cur_node.next
            self._cur_index += 1
        return node


def test_answer():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() is 3
    assert stack.pop() is 2
    assert stack.pop() is 1
    assert stack.pop() is None


def test_iterator():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    a = []
    for i in stack:
        a.append(i.item)
    assert a == [3, 2, 1]
