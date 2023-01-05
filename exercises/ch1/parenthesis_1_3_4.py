import sys

from adt.LinkedListStack import Stack


def is_valid(st: str):
    valid = False
    stack = Stack()
    for c in st:
        if c == "[" or c == "{" or c == "(":
            stack.push(c)
        else:
            o = stack.pop()
            if not ((o == "[" and c == "]") or (o == "{" and c == "}") or (o == "(" and c == ")")):
                valid = False
            else:
                valid = True
    return valid


if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(s)
    print(is_valid(s))


def test_inputs():
    assert is_valid("{}(){()}[{()}]") is True
    assert is_valid("{{}}]") is False
    assert is_valid("{{}}") is True
