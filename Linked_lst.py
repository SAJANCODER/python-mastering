class Linked:
    def __init__(self,data):
        self.data=data
        self.next=None
a = Linked(10)
b= Linked(20)
c = Linked(30)

head = a

a.next=b
b.next=c

f = Linked(15)
f.next=b

a.next=f

current = head

while current:
    print(current.data)
    current=current.next
