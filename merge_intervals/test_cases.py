from merge_intervals import merge

def test_merge():
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]
    print("All tests passed.")

if __name__ == "__main__":
    test_merge()