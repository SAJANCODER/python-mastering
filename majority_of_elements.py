arr = list(map(int,input("Enter the array:").split(" ")))
target = len(arr)//2
hashmap = {}
final_majority = 0
for i in arr:
    if i in hashmap:
        hashmap[i]+=1
        if hashmap[i]>=target:
            final_majority= i
    else:
        hashmap[i]=1
print(final_majority)


        
