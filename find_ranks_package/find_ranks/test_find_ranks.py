from find_ranks import find_ranks

def test_case_1():
    assert find_ranks([10, 3, 8, 9, 4]) == ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']

def test_case_2():
    assert find_ranks([5, 4, 3, 2, 1]) == ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']

def test_case_3():
    assert find_ranks([1]) == ['Gold Medal']

print("All test cases passed!")
