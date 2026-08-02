class linked_list:
    def __init__(self,data):
        self.data=data
        self.next=None
ll=list(map(int,input("Enter the linkedlist elements: ").split(" ")))
master_head = None
current = None
leng=0
for i in ll:
    x = linked_list(i)
    if master_head is None:
        master_head = x
        current=x
        leng+=1
    else:
        current.next=x
        current=current.next
        leng+=1

current = master_head
prev = linked_list(0)
dummy = prev
while current:
    first = current
    second = current.next
    next_pair = second.next
    prev.next = second
    second.next = first
    first.next = next_pair
    prev = first
    current = next_pair


    

current=dummy.next
while current:
    print(current.data)
    current=current.next
