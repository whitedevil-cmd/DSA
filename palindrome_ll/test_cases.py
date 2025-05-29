from palindrome_ll import ListNode, is_palindrome

def build_list(values):
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_is_palindrome():
    assert is_palindrome(build_list([1,2,2,1]))
    assert not is_palindrome(build_list([1,2]))
    print("All tests passed.")

if __name__ == "__main__":
    test_is_palindrome()