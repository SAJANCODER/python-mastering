#Count Occurrences of Each Element
arr = input("Enter the word:").strip()
hash = {}
for i in arr:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
print(hash)