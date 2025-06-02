from add_linked_lists import create_list, add_list, print_list

def test_add_list():
    l1 = create_list([2, 4, 3])
    l2 = create_list([5, 6, 4])
    result = add_list(l1, l2)
    assert print_list(result) == "7->0->8"

    l1 = create_list([0])
    l2 = create_list([0])
    result = add_list(l1, l2)
    assert print_list(result) == "0"

    l1 = create_list([9, 9, 9, 9, 9, 9, 9])
    l2 = create_list([9, 9, 9, 9])
    result = add_list(l1, l2)
    assert print_list(result) == "8->9->9->9->0->0->0->1"

test_add_list()
print("All tests passed.")
