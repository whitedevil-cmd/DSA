class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_list(current):
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    return "->".join(result)

def add_list(list1, list2):
    dummy = Node()
    current = dummy
    carry = 0

    while list1 or list2 or carry:
        val1 = list1.val if list1 else 0
        val2 = list2.val if list2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)
        current = current.next
        if list1:
            list1 = list1.next
        if list2:
            list2 = list2.next
    return dummy.next
