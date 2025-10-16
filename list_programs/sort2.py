#Check if a list is sorted.
lst = list(map(int,input("Enter a list:").split()))
sorted = True
n=len(lst)
for i in range(n-1):
    if lst[i]>lst[i+1]:
        sorted = False
        break
if sorted:
    print("The List is intially sorted")
else:
    print("The List is not sorted")