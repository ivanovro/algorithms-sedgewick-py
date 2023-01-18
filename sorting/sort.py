class Sort:
    def __init__(self, a: list):
        self.a = a

    def is_sorted(self):
        for i in range(1, len(self.a)):
            if self.a[i - 1] > self.a[i]:
                return False
        return True
