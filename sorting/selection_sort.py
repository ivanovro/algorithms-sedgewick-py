import sorting.sort


class SelectionSort(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        for i in range(0, len(a)):
            for j in range(i, len(a)):
                if a[i] > a[j]:
                    a[j], a[i] = a[i], a[j]


def test_sort():
    ss = SelectionSort([1, 88, 2, 9, 2, 3, 9])
    assert ss.is_sorted()
    assert ss.a == [1, 2, 2, 3, 9, 9, 88]
