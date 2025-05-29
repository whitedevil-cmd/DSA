from valid_parentheses import is_valid

def test_is_valid():
    assert is_valid("()")
    assert is_valid("()[]{}")
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert is_valid("{[]}")
    print("All tests passed.")

if __name__ == "__main__":
    test_is_valid()