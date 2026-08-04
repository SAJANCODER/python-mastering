x = input("Enter a number: ")
presses = 0
# arr = []

# for i in x:
#     arr.append(i)
# m = arr.copy()

# j=0
# while j<len(arr)-1:
#     if arr[j]=='0' and arr[j+1]=='0':
#         presses+=1
#         m.remove(arr[j])
#         m.remove(arr[j+1])
#         j+=2
#     else:
#         j+=1
# print(m)
# j = presses + (len(m))
# print(j)

i=0
while i<len(x):
    if (i+1)<len(x) and x[i]=='0' and x[i+1]=='0':
        presses+=1
        i+=2
    else:
        presses+=1
        i+=1
print(presses)