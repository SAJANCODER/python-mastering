val=input()
left,right = val.split("=")

if "+" in left:
    num1,num2 = left.split("+")
elif "-" in left:
    num1,num2=left.split("-")
elif "*" in left:
    num1,num2=left.split("*")
elif "/" in left:
    num1,num2=left.split("/")
x=int(num1)
y=int(num2)
z=int(right)

if x*y==z:
    print("*")
elif x-y==z:
    print("-")
    
elif x//y==z:
    print("/")
elif x+y==z:
    print("+")
