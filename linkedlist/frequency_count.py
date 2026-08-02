a = input("Enter the name: ")
hash = {}
found = False
for i in a:
    if i not in hash:
        hash[i]=1

    else:
        hash[i]+=1
for key,values in hash.items():
    if values==1:
        print(key,values)
        found = True
        break

    
if not found:
    print("-1")     