class linked_list:
    def __init__(self,data):
        self.data = data
        self.next = None
arr = list(map(int,input("Enter the linked list elements:").split(" ")))
k = int(input("Enter rotation:"))
head = None
current = None
prev = None
leng = 0
for i in arr:
    ll = linked_list(i)
    if head  is None:
        head = ll
        current = ll
        leng+=1
    else:
        prev = current
        current.next = ll
        current=current.next
        leng+=1

k = k%leng
for i in range(k):
    current = head
    while current.next.next:
        current = current.next
    last_node = current.next
    current.next = None
    last_node.next = head
    head = last_node
current = head
while current:
    print(current.data)
    current = current.next


