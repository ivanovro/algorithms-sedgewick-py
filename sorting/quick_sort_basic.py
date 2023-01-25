import sorting.sort


class QuickSortBasic(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        self._sort(0, len(a) - 1)

    def recursion_counter(self) -> int:
        return self.cnt

    def _sort(self, lo: int, hi: int):
        if hi <= lo:
            return
        p = self._partition(lo, hi)
        self._sort(lo, p - 1)
        self._sort(p + 1, hi)

    def _partition(self, lo: int, hi: int) -> int:
        v = self.a[lo]
        i, j = lo + 1, hi
        while True:
            while self.a[i] < v:
                i += 1
                if i == hi:
                    break
            while self.a[j] > v:
                j -= 1
                if j == lo:
                    break
            if i >= j:
                break
            self.a[i], self.a[j] = self.a[j], self.a[i]
        self.a[lo], self.a[j] = self.a[j], self.a[lo]
        return j


def test_sorting():
    a = [1, 88, 2, 9, 2, 3, 9]
    qs = QuickSortBasic(a)
    assert qs.is_sorted()
    assert qs.a == [1, 2, 2, 3, 9, 9, 88]
