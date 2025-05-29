from binary_search import binary_search

def test_binary_search():
    assert binary_search([1,2,3,4,5,6], 4) == 3
    assert binary_search([1,2,3,4,5,6], 1) == 0
    assert binary_search([1,2,3,4,5,6], 6) == 5
    assert binary_search([1,2,3,4,5,6], 7) == -1
    print("All tests passed.")

if __name__ == "__main__":
    test_binary_search()