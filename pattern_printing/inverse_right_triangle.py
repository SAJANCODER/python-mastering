n = int(input("Enter the value:"))
x=0
for i in range(n,0,-1):
    x = n-i
    print(x*" ",end="")
    for j in range(i):
        print("#",end="")
    print()
