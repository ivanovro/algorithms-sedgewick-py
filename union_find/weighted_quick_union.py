class WeightedQuickUnion:
    def __init__(self, n: int):
        self.count = n
        self.id = [i for i in range(0, n)]
        self.sz = [1 for _ in range(0, n)]

    def connected(self, i: int, j: int):
        return self.find(i) == self.find(j)

    def find(self, p: int):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        self.count -= 1


def test_uf():
    uf = WeightedQuickUnion(10)
    assert uf.connected(2, 3) is False
    uf.union(2, 3)
    assert uf.connected(2, 3) is True
    uf.union(4, 3)
    uf.union(6, 3)
    assert uf.connected(6, 3) is True
    assert uf.count == 7
