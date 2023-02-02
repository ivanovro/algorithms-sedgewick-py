import sorting.sort


class HeapSort(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        self.n = len(a) - 1
        # construct the heap from the middle to form sub-heaps of size greater than 1
        for k in range(int(self.n / 2), 0, -1):
            self.sink(k)
        # take from the top and put to the bottom
        while self.n > 1:
            self.exchange(1, self.n)
            self.n -= 1
            self.sink(1)

    def sink(self, i: int):
        while 2 * i <= self.n:
            j = i * 2
            if j + 1 <= self.n and self.a[j] < self.a[j + 1]:
                j += 1
            if self.a[i] >= self.a[j]:
                break
            self.exchange(i, j)
            i = j

    def exchange(self, i: int, j: int):
        self.a[i], self.a[j] = self.a[j], self.a[i]


def test_sort():
    a = [None, 234, 8, 0, 3, 89, 10]
    hs = HeapSort(a)
    assert hs.is_sorted(2)
    assert a == [None, 0, 3, 8, 10, 89, 234]
