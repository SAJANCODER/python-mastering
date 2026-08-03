a = input("Enter the string:")
operation = int(input("Enter the number of operations:"))
arr = list(map(int,input("Enter the operations: ").split(" ")))
x= a
for i in arr:
    if i==1:
        x = x[-1] + x[1:3] + x[0]  #DBCA 
    if i==2:
            mid = len(a)//2
            x = x[mid:] + x[:mid]
            
print(x)