class linked_list:
    def __init__(self,data):
        self.data=data
        self.next=None
ll=list(map(int,input("Enter the linkedlist elements: ").split(" ")))
n = int(input("Enter the position you need to remove: "))
head = None
current = None
leng=0
for i in ll:
    x = linked_list(i)
    if head is None:
        head = x
        current=x
        leng+=1
    else:
        current.next=x
        current=current.next
        leng+=1
current = head
linked_list_len = leng - n
if linked_list_len == 0:
    head = head.next
for i in range(linked_list_len-1):
    print("Current data",current.data)
    current = current.next

print("Final current position:",current.data)
last_node = current.next.next
current.next = last_node
current = head
while current:
    print(current.data)
    current=current.next