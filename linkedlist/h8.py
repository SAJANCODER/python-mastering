#Find the Missing Number
arr = list(map(int,input("Enter the values:").split()))
seen = set(arr)
for i in range(1,max(arr)+1):
    if i not in seen:
        print("Missing value is : ",i)
        