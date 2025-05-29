"""
Title: Double a Number Represented by a Linked List
Difficulty: Easy

You are given a singly linked list where each node contains a single digit.
The digits are stored in reverse order (least significant digit comes first).
Your task is to double the number and return the result as a linked list
in normal order (most significant digit comes first).
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_reversed_LL(values):
    head = Node(values[-1])
    current = head
    for value in reversed(values[:-1]):
        current.next = Node(value)
        current = current.next
    return head

def reverseLL(head):
    prev = None
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def double_LL(head):
    if not head:
        return None
    current = head
    carry = 0
    prev = None
    while current:
        doubled = current.val * 2 + carry
        current.val = doubled % 10
        carry = doubled // 10
        prev = current
        current = current.next
    if carry:
        prev.next = Node(carry)
    return reverseLL(head)

def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)
