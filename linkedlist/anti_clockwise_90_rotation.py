n=int(input("Enter the length:"))
arr = []
for i in range(1,n+1):
    lst = list(map(int,input("Enter the array elemets: ").split(" ")))
    if len(lst) == n:
        arr.append(lst)
    else:
        print(f"{n}x{n} exceed" if len(lst)>n else f"{n}x{n} is lesser")
# col = n-1
row = n-1
page = []
final_arr=[]
for i in range(len(arr)-1,-1,-1):
    for j in range(len(arr)):
        page.append(arr[j][i])  
    final_arr.append(page)
    page=[]
for i in final_arr:
    x=list(map(str,i))
    print(" ".join(x))