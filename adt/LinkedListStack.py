class Stack:
    class Node:
        def __init__(self, item: object):
            self.next = None
            self.item = item

    def __init__(self):
        self.first = None
        self.n = 0

    def push(self, item: object):
        old_first = self.first
        self.first = self.Node(item)
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


def test_answer():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() is 3
    assert stack.pop() is 2
    assert stack.pop() is 1
    assert stack.pop() is None
