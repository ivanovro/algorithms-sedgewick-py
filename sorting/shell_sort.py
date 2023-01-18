import sorting.sort


class ShellSort(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        for h in [5, 3, 1]:
            for i in range(0, len(a), h):
                j = i + h
                while h <= j < len(a) and a[j - h] > a[j]:
                    a[j], a[j - h] = a[j - h], a[j]
                    j -= h


def test_sort():
    ss = ShellSort([1, 88, 2, 999, 24, 19, 222, 400, 245, 9, 2, 3, 9, 234, 90, 21, 34, 123, 909, 23, 93, 55, 22])
    assert ss.is_sorted()
