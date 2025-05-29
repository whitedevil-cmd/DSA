from queue_using_stacks import MyQueue

def test_queue():
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
    print("All tests passed.")

if __name__ == "__main__":
    test_queue()