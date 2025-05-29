from maximum_subarray import max_sub_array

def test_max_sub_array():
    assert max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5,4,-1,7,8]) == 23
    print("All tests passed.")

if __name__ == "__main__":
    test_max_sub_array()