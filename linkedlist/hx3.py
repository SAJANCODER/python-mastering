#First Non-Repeating Character\
a = input("Enter a word:").strip()
hash = {}
for i in a:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1
for j in a:
    if hash[j]==1:
        print(j)
        break