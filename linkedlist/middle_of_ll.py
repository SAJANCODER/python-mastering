class Linked_List:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Linked_List(1)
b = Linked_List(2)
c = Linked_List(3)
d = Linked_List(4)
e = Linked_List(5)

a.next=b
b.next=c
c.next=d
d.next = e
head = a
current = head 

linked_sum = 0
leng = 0
while current:
    leng+=1
    current = current.next
current = head
middle_len = leng//2
new_len = 0
for i in range(middle_len):
    current = current.next
print(current.data)
