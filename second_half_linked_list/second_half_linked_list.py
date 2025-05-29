# second_half_linked_list.py

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values):
    """Creates a singly linked list from a list of values and returns the head node."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_list(head):
    """Prints the linked list in a readable format."""
    if not head:
        print("[]")
        return
    current = head
    print("[", end="")
    while current:
        print(current.val, end="," if current.next else "]\n")
        current = current.next

def second_half(head):
    """
    Returns the head of the second half of the linked list.
    For odd-length lists, the middle node is considered part of the second half.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Input and execution
if __name__ == "__main__":
    values = list(map(int, input("Enter list: ").strip().split()))
    head = create_linked_list(values)
    head = second_half(head)
    print_list(head)
