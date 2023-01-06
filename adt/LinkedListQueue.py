from adt.Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def enqueue(self, item: object):
        old_last = self.last
        self.last = Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.n += 1

    def dequeue(self) -> object:
        if self.is_empty():
            return None
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        if self.is_empty():
            self.last = None
        return item

    def is_empty(self):
        return self.n is 0
