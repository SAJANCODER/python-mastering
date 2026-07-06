class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(5)
b=Node(15)
c=Node(25)
d=Node(35)

a.next=b
b.next=c
c.next=d

head=a

current=head
while current:
    print(current.data)
    current=current.next
    



