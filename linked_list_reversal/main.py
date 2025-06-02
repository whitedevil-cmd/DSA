class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversed_list(head, left, right):
    if not head or left == right:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next

def create_list(arr):
    dummy = Node(0)
    current = dummy
    for val in arr:
        current.next = Node(val)
        current = current.next
    return dummy.next

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    head = create_list(list(input("list: ").strip().split(" ")))
    left = int(input("left= "))
    right = int(input("right= "))
    head = reversed_list(head, left, right)
    print_list(head)
