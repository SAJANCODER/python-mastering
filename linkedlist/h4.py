#Contains Duplicate 
arr = list(map(int,input("enter the array values: ").split()))
status = False
hash={}
for i in arr:
    if i in hash:
        status = True
        break
    hash[i]=1
print("Contains Duplicate : ",status)