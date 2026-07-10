#Character Frequency using a Dictionary 
a = input("Enter the word: ").strip()

hash={}
for i in a:
    if i in hash:
        
        hash[i] +=1
    else:
        hash[i]=1
for i in hash.items():
    print(i)