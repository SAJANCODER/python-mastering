n = int(input("Enter the number:"))
x=n
for i in range(1,n+1):
    x=n-i
    print(x*" ",end="")
    for j in range(i):
        print("*",end="")
        
    print()