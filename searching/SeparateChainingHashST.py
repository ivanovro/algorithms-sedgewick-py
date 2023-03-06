from adt.SequentialSearchST import SequentialSearchST


class SeparateChainingHashST:
    def __init__(self, m: int):
        self.m = m
        self.st = [SequentialSearchST() for _ in range(0, m)]

    def _hash(self, key):
        return hash(key) % self.m

    def put(self, key, value):
        self.st[self._hash(key)].put(key, value)

    def get(self, key):
        return self.st[self._hash(key)].get(key)


def test_st():
    st = SeparateChainingHashST(8)
    assert len(st.st) == 8

    st.put("a", 1)
    assert st.get("a") == 1

    st.put("a", 2)
    st.put("b", 39)
    st.put("c", 400)

    assert st.get("b") == 39
    assert st.get("a") == 2
    assert st.get("c") == 400

