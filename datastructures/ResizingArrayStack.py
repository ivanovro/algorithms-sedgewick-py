class ResizingArrayStack:
    def __init__(self):
        self.a = [None]  # array holding elements
        self.n = 0  # number of elements in the stack

    def is_empty(self):
        return self.n == 0

    def size(self):
        return self.n

    def resize(self, max: int) -> None:
        b = [None] * max
        for i in range(0, self.n):
            b[i] = self.a[i]
        self.a = b

    def push(self, o: object):
        if self.n == len(self.a):
            self.resize(self.n * 2)
        self.a[self.n] = o
        self.n += 1

    def pop(self):
        if self.n == 0:
            return 
        self.n -= 1
        item = self.a[self.n]
        self.a[self.n] = None
        if self.n > 0 and self.n == int(len(self.a) / 4):
            self.resize(int(len(self.a) / 2))
        return item


if __name__ == "__main__":
    ras = ResizingArrayStack()
    ras.push(1)
    ras.push(2)
    ras.push(3)
    print(ras.pop())
    print(ras.pop())
    print(ras.pop())
    print(ras.pop())
