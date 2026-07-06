arr = list(map(int,input().split(" "))) #4 5 6 7
target= int(input("Enter your target:")) #10
for i in range(len(arr)): #4
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)
