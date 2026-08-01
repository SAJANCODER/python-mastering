# 📅 Day 7 Challenge: Reorder List

# Difficulty: Medium
# LeetCode: Reorder List

# Problem Statement

# Given the head of a singly linked list:

# L0 → L1 → L2 → ... → Ln

# Reorder it to:

# L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

# You must not change the values inside the nodes. Only modify the links.

# Example 1

# Input

# 1 → 2 → 3 → 4

# Output

# 1 → 4 → 2 → 3
# Example 2

# Input

# 1 → 2 → 3 → 4 → 5

# Output

# 1 → 5 → 2 → 4 → 3
# Constraints
# Do not create a new linked list.
# Do not use an array or stack to store all nodes.
# Modify only the next pointers.
# Aim for O(n) time and O(1) extra space.

class linked_list:
    def __init__(self,data):
        self.data = data
        self.next = None
ll=list(map(int,input("Enter the linked list elements: ").split(" ")))
master_head = None
current = None
for i in ll:
    x= linked_list(i)
    if master_head is None:
        master_head = x
        current = x
    else:
        current.next = x
        current = current.next

current = master_head
# while current:
#     print(current.data)
#     current=current.next

#---> to find middle element use slow fast approach pointer

slow = master_head  #-->middle element
fast = master_head
prev = None
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

second_list = slow.next
first_list = slow
slow.next = prev

current = second_list
while current:
    element = current.next
    current.next=prev
    prev = current
    current = element
second_list_node = prev
# while current:
#     print(current.data)
#     current=current.next
first_list_node = master_head
while second_list_node:
    next_node = first_list_node.next
    second_next_node = second_list_node.next
    first_list_node.next = second_list_node
    second_list_node.next = next_node
    first_list_node = next_node
    second_list_node = second_next_node

current = master_head
while current:
    print(current.data)
    current=current.next



