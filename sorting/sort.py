class Sort:
    def __init__(self, a: list):
        self.a = a

    def is_sorted(self, start: int = 1):
        for i in range(start, len(self.a)):
            if self.a[i - 1] > self.a[i]:
                return False
        return True
