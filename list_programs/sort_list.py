#make a list in asc order
lst = list(map(int,input("Enter a list: ").split()))
n = len(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i] > lst[j]:
            lst[i] , lst[j] = lst[j] , lst[i]
print(f"Sorted List is : {lst}")
