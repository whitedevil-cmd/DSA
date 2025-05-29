from flood_fill import flood_fill

def test_flood_fill():
    assert flood_fill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2) == [[2,2,2],[2,2,0],[2,0,1]]
    print("All tests passed.")

if __name__ == "__main__":
    test_flood_fill()