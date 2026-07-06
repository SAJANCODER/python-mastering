arr = list(map(int,input("Enter the array values: ").split(" ")))
target = int(input("Enter the value: "))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)
