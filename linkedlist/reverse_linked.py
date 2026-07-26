class Linked_List:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Linked_List(1)
b = Linked_List(2)
c = Linked_List(3)
d = Linked_List(4)

a.next = b
b.next = c
c.next = d

head = a
current = head
prev = None

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    
head = prev
current = head
while current:
    print(current.data)
    current = current.next