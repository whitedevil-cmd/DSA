"""
Unit tests for double_linked_list.py
"""

from double_linked_list import Node, create_reversed_LL, double_LL

def list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def test_double_LL():
    # Test 1
    head = create_reversed_LL([1, 2, 3])  # represents 321
    result = double_LL(head)
    assert list_to_array(result) == [6, 4, 2], "Test 1 Failed"

    # Test 2
    head = create_reversed_LL([9, 9, 9])  # represents 999
    result = double_LL(head)
    assert list_to_array(result) == [1, 9, 9, 8], "Test 2 Failed"

    # Test 3
    head = create_reversed_LL([0])  # represents 0
    result = double_LL(head)
    assert list_to_array(result) == [0], "Test 3 Failed"

    # Test 4
    head = create_reversed_LL([5])  # represents 5
    result = double_LL(head)
    assert list_to_array(result) == [1, 0], "Test 4 Failed"

    print("All tests passed.")

if __name__ == "__main__":
    test_double_LL()
