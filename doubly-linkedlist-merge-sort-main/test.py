
---

### 🧪 `test.py`

```python
from doubly_merge_sort import create_doublyLL, merge_sort, print_list

def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_case(values):
    head = create_doublyLL(values)
    sorted_head = merge_sort(head, len(values))
    return to_list(sorted_head)

def run_tests():
    tests = [
        ([], []),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 1, 3, 1, 2], [1, 1, 2, 3, 4]),
        ([7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7])
    ]

    passed = 0
    for i, (input_list, expected) in enumerate(tests, 1):
        result = test_case(input_list)
        if result == expected:
            print(f"Test {i}: ✅ Passed")
            passed += 1
        else:
            print(f"Test {i}: ❌ Failed — Expected {expected}, got {result}")
    print(f"\n{passed}/{len(tests)} tests passed.")

if __name__ == "__main__":
    run_tests()
