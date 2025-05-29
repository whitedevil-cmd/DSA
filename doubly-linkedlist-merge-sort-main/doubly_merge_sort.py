class Node:
  def __init__(self,val=0,next=None,prev=None):
    self.val=val
    self.next=next
    self.prev=prev
def print_list(head):
  if not head:
    print("[]")
    return 
  current=head
  print(current.val,end="")
  current=current.next
  while current:
    print(f" <-> {current.val}",end="")
    current=current.next
def create_doublyLL(values):
  if not values:
    return None
  head=Node(values[0])
  current=head
  current.prev=None
  for i in values[1:]:
    current.next=Node(i)
    current.next.prev=current
    current=current.next
  return head
def split(head,size):
  mid=size//2
  current=head
  for _ in range(mid-1):
    current=current.next
  second=current.next
  if second:
    second.prev=None
  current.next=None
  return head,second
def merge(head,second):
  if not head:
    return second
  if not second:
    return head
  if head.val<second.val:
    head.next=merge(head.next,second)
    if head.next:
      head.next.prev=head
    head.prev=None
    return head
  else:
    second.next=merge(second.next,head)
    if second.next:
      second.next.prev=second
    second.prev=None
    return second
def merge_sort(head,size):
  if not head: 
    return None
  if size<=1:
    return head
  mid=int(size/2)
  left,right=split(head,size)
  left_size=size//2
  right_size=size - left_size
  left=merge_sort(left,left_size)
  right=merge_sort(right,right_size)
  return merge(left,right)
size=int(input("enter size:"))
values=list(map(int,input("enter values:").strip().split()))  
head=create_doublyLL(values)
sorted=merge_sort(head,size)
print_list(sorted)
