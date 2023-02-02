class HeapMaxPQ:
    def __init__(self):
        self.n = 0
        self.pq = []
        self.pq.append(None)

    def insert(self, o: object):
        self.n += 1
        self.pq.append(o)
        self.swim(self.n)

    def del_max(self):
        if len(self.pq) == 0:
            return None
        max_el = self.pq[1]
        self.exchange(1, self.n)
        self.pq[self.n] = None
        self.n -= 1
        self.sink(1)
        return max_el

    def swim(self, i: int):
        k = int(i / 2)
        while k > 0 and self.pq[k] < self.pq[i]:
            self.exchange(k, i)
            i = k
            k = int(k / 2)

    def sink(self, i: int):
        while 2 * i <= self.n:
            j = i * 2
            if j + 1 <= self.n and self.pq[j] < self.pq[j + 1]:
                j += 1
            if self.pq[i] >= self.pq[j]:
                break
            self.exchange(i, j)
            i = j

    def exchange(self, i: int, j: int):
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]


def test_pq():
    pq = HeapMaxPQ()
    pq.insert(5)
    pq.insert(1)
    pq.insert(10)
    pq.insert(12)
    pq.insert(3)
    a = []
    for i in range(0, pq.n):
        a.append(pq.del_max())
    assert a == [12, 10, 5, 3, 1]
