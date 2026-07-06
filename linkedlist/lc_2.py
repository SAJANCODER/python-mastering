class li:
    def __init__(self,data):
        self.data=data
        self.next=None
a=li(2)
b=li(4)
c=li(3)

a.next=b
b.next=c

l1 = a

d=li(5)
e=li(6)
f=li(4)

d.next=e
e.next=f

l2=d

current = l1
current1=l2

carry=0
digit = 0
new_lst = []
while current and current1:
    total = current.data + current1.data +carry
    if total>=10:
        total1 = total//10
        carry = total1
        digit = total%10
        new_lst.append(digit)
    else:    
        new_lst.append(total)
    current = current.next
    current1=current1.next
print(new_lst)
