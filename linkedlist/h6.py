#Remove Duplicates from an Array 
arr = list(map(int,input("Enter the value : ").split(" ")))
hash={}
result = []
for i in arr:
    if i not in hash:
        hash[i]=True
        result.append(i)
print(result)