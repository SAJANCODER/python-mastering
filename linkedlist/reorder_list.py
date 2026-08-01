class linked_list:
    def __init__(self,data):
        self.data = data
        self.next = None
ll = list(map(int,input("Enter the linked list values: ").split(" ")))

head = None
current = None
last_val = 0
for i in ll:
    x = linked_list(i)
    if head is None:
        head = x
        current=x
    else:
        current.next = x
        current = x
        last_val = current

slow = head
fast = head
prev = None

while fast.next:
    slow = slow.next
    fast = fast.next.next
    
second_list = slow.next
slow.next = prev
master_head = head
current = head
while current:
    print(current.data)
    current=current.next

current = second_list
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
head = prev
current = head
while current:
    print(current.data)
    current=current.next

current = master_head
first_current = master_head
second_current = prev

while second_current:
    first_next = first_current.next
    second_next = second_current.next
    first_current.next = second_current
    second_current.next = first_next
    first_current = first_next
    second_current = second_next
    current = first_current.next
    
current = head
while current:
    print(current.data)
    current=current.next