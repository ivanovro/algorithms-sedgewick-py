class QuickFind:
    def __init__(self, n: int):
        self.count = n
        self.id = [i for i in range(0, n)]

    def connected(self, i: int, j: int):
        return self.find(i) == self.find(j)

    def find(self, p: int):
        return self.id[p]

    def union(self, p: int, k: int):
        p = self.find(p)
        k = self.find(k)

        if p == k:
            return
        for i in range(0, len(self.id)):
            if self.id[i] == p:
                self.id[i] = k
        self.count -= 1


def test_uf():
    uf = QuickFind(10)
    assert uf.connected(2, 3) is False
    uf.union(2, 3)
    assert uf.connected(2, 3) is True
    uf.union(4, 3)
    uf.union(6, 3)
    assert uf.connected(6, 3) is True
    assert uf.count == 7
