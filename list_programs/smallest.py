num = list(map(int,input("enter the numbers:").split()))
smallest = num [0]
for i in num :
    if i < smallest:
        smallest = i
print(f"SMALLEST NUMBER : {smallest}")