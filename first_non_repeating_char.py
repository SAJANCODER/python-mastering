char = input("Enter the string:")
has = {}
for i in char:
    if i in has:
        has[i]+=1
    else:
        has[i] = 1
for j in has:
    if has[j]==1:
        print(j)
        break
    
