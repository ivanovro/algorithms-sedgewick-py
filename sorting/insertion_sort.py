import sorting.sort


class InsertionSort(sorting.sort.Sort):
    def __init__(self, a: list):
        super().__init__(a)
        for i in range(0, len(a)):
            j = i + 1
            while 1 <= j < len(a) and a[j - 1] > a[j]:
                a[j], a[j - 1] = a[j - 1], a[j]
                j -= 1


def test_sort():
    ss = InsertionSort([1, 88, 2, 9, 2, 3, 9])
    assert ss.is_sorted()
