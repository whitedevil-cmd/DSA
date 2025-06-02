from remove_node_doubly_linked_list_v2 import create_list, remove_node, print_list

def test_remove_node():
    head = create_list([1, 2, 3, 2, 4, 2, 5])
    result = remove_node(head, 2)
    assert print_list(result) == "1<->3<->4<->5"

    head = create_list([2, 2, 2])
    result = remove_node(head, 2)
    assert print_list(result) == ""

    head = create_list([1, 2, 2, 3])
    result = remove_node(head, 2)
    assert print_list(result) == "1<->3"

    head = create_list([])
    result = remove_node(head, 2)
    assert print_list(result) == ""

if __name__ == "__main__":
    test_remove_node()
    print("All tests passed.")
