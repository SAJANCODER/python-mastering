# # Problem: Remove the Nth Node From the End of the List

# # Example:

# # Input:
# # 1 → 2 → 3 → 4 → 5

# # n = 2

# # Output:

# # 1 → 2 → 3 → 5

# # Because the 2nd node from the end is 4.

class Linked_list:
    def __init__(self,digits):
        self.digits = digits
        self.next = None
ll_val = list(map(int,input("Enter the linked_list values:").split(" ")))
head = None
current = None
x = int(input("Enter the nth length to remove (like index=1 or n): "))
# del_val = (len(ll_val) - x) 
# previous_val = del_val-1
leng=0

for i in ll_val:
    ll_list = Linked_list(i)
    if head is None:
        head = ll_list
        current = ll_list
        leng+=1
    else:
        current.next = ll_list
        current = ll_list
        leng+=1
current = head

# if del_val==0:
#     head = head.next
# for i in range(previous_val):
#     current = current.next

# current.next = current.next.next

# current = head
# while current:
#     print(current.digits)
#     current = current.next

#optimized
dummy = Linked_list(0)
dummy.next=head
slow = dummy
fast = dummy

for i in range(x):
    fast = fast.next
while fast.next:
    slow=slow.next
    fast=fast.next
slow.next = slow.next.next
current = dummy.next
while current:
    print(current.digits)
    current = current.next