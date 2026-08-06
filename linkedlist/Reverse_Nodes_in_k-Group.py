class linkedlist:
    def __init__(self,data):
        self.data = data
        self.next=None
arr = list(map(int,input("Enter the linked list elements: ").split(" ")))
k = int(input("Enter the number :"))
head = None
current = None
for i in arr:
    l =  linkedlist(i)
    if head is None:
        head = l
        current = l
    else:
        current.next = l
        current = current.next
current = head
# while current:
#     print(current.data)
#     current = current.next

prev = None
while current:
    next_node = current.next
    current.next=prev
    prev=current
    current=next_node
current = head
while current:
    print(current.data)
    current=current.next