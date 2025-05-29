from climbing_stairs import climb_stairs

def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    print("All tests passed.")

if __name__ == "__main__":
    test_climb_stairs()