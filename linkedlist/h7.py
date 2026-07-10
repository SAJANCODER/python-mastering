#Find the Majority Element 
arr = list(map(int,input("Enter the value :").split()))
hash = {}
for i in arr:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
for key,value in hash.items():
    if value>len(arr)//2:
        print("Majority Element is :",key)
        break
    else:
        print("No Majority exists")