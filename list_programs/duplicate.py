# duplicate numbers in the list
num = list(map(int,input("enter the list numbers:").split()))
uni = []
dup = []
for i in num:
    if i not in uni:
        uni.append(i)
    else:
        dup.append(i)
print("Duplicated Values : ", dup)