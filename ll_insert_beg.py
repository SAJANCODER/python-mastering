class Ln:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Ln(10)
b=Ln(20)
c=Ln(30)

a.next=b
b.next=c

head = a
new = Ln(5)
new.next= head

head = new 

current =head
while current:
    print(current.data)
    current=current.next
