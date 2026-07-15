#Count frequency of each character using dictionary.
a = input("Enter the word: ")
hash = {}
for i in a:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
print(hash)