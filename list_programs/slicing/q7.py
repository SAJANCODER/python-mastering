#Swap the first half and the second half of a list using slicing.
#Example: [1,2,3,4,5,6] → [4,5,6,1,2,3]

num = list(map(int,input("Enter the list:").split()))
mid = len(num)//2
if len(num)%2==0:
    rotate = num[-mid:]+num[:mid]
    print(f"Before Swap: {num}")
    print(f"After Swap(Even): {rotate}")
else:
    rotate = num[mid+1:] + [num[mid]] + num[:mid]
    print(f"Before Swap: {num}")
    print(f"After Swap(Odd): {rotate}")



