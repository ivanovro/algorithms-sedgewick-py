class SequentialSearchST:
    class Node:
        def __init__(self, key=None, value=None, next=None):
            self.next = next
            self.key = key
            self.value = value

    def __init__(self):
        self.first = self.Node()

    def get(self, key):
        node = self.first
        while node is not None and node.key != key:
            node = node.next
        else:
            return node.value if node is not None else None

    def put(self, key, value):
        node = self.first
        while node is not None and node.key != key:
            node = node.next
        else:
            if node is None:
                self.first = self.Node(key, value, self.first)
            else:
                node.value = value


def test_st():
    st = SequentialSearchST()

    st.put("a", 1)
    assert st.get("a") == 1

    st.put("a", 2)
    st.put("b", 3)
    st.put("c", 4)

    assert st.get("b") == 3
    assert st.get("a") == 2
    assert st.get("c") == 4

    assert st.first.key == "c"
    assert st.first.next.key == "b"
    assert st.first.next.next.key == "a"
