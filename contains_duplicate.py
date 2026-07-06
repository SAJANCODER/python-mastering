arr = list(map(int,input("Enter the array:").split(" ")))
status = False
count = {}
for i in arr:
    if i in count:
        count[i] +=1
        if count[i]>1:
            status = True
    else:
        count[i] =1

print(status)
