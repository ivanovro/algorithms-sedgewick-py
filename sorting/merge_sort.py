import sorting.sort


class MergeSort(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        self.aux = [0 for _ in a]
        self.sort(0, len(self.aux) - 1)

    def sort(self, lo: int, hi: int):
        if hi <= lo:  # base case, one element
            return
        mid = int(lo + (hi - lo) / 2)
        self.sort(lo, mid)
        self.sort(mid + 1, hi)
        self.merge(lo, mid, hi)

    def merge(self, lo: int, mid: int, hi: int):
        i, j = lo, mid + 1

        for k in range(lo, hi + 1):  # range is start inclusive, stop exclusive
            self.aux[k] = self.a[k]

        for k in range(lo, hi + 1):
            if i > mid:  # left side is finished
                self.a[k] = self.aux[j]
                j += 1
            elif j > hi:  # right side is finished
                self.a[k] = self.aux[i]
                i += 1
            elif self.aux[i] > self.aux[j]:  # right element is smaller
                self.a[k] = self.aux[j]
                j += 1
            else:  # left element is smaller
                self.a[k] = self.aux[i]
                i += 1


def test_sorting():
    a = [1, 88, 2, 9, 2, 3, 9]
    ms = MergeSort(a)
    assert ms.is_sorted()
    assert ms.a == [1, 2, 2, 3, 9, 9, 88]
