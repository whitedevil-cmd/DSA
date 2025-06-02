class Node:
    def __init__(self, prev=None, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = prev

def create_list(values):
    if not values:
        return None
    head = Node(val=values[0])
    current = head
    for value in values[1:]:
        current.next = Node(val=value, prev=current)
        current = current.next
    return head

def print_list(head):
    if not head:
        return ""
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    return "<->".join(result)

def remove_node(head, target):
    if not head:
        return None
    while head and head.val == target:
        head = head.next
        if head:
            head.prev = None
    current = head
    while current:
        if current.next and current.next.val == target:
            temp = current.next
            current.next = temp.next
            if temp.next:
                temp.next.prev = current
        else:
            current = current.next
    return head
