x = int(input("Enter the length: "))
arr = list(map(int,input("Enter the array elements:").split(" ")))
special = 0
for i in range(x):
    left = 0
    right = 0

    #for left
    for j in range(i):
        if arr[j]>arr[i]:
            left+=1
    #for right
    for s in range(i+1,x):
        if arr[s]>arr[i]:
            right+=1
    if left>right:
        special+=1
print(special)