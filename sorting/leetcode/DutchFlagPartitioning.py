import sorting.sort


class DutchFlagPartitioning(sorting.sort.Sort):
    def __init__(self, a: list):
        super(DutchFlagPartitioning, self).__init__(a)
        red, white, blue = 0, 0, len(a) - 1
        while white <= blue:
            if a[white] == 0:
                a[red], a[white] = a[white], a[red]
                red += 1
                white += 1
            elif a[white] == 1:
                white += 1
            else:
                a[white], a[blue] = a[blue], a[white]
                blue -= 1


def test_partitioning():
    a = [1, 0, 2, 2, 1, 0, 0]
    dfp = DutchFlagPartitioning(a)
    assert dfp.is_sorted()
    assert a == [0, 0, 0, 1, 1, 2, 2]
