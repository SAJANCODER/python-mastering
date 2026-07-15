#Find the smallest subarray whose sum is greater than or equal to S = 7. [2,1,5,2,3,2] o/p =2
arr=list(map(int,input("Enter the array:").split()))
s=7
current = 0
left = 0
max1 = float('inf')
start = 0
end = 0
for i in range(len(arr)):
    current+=arr[i]
    if current == s:
        start = left
        end = i 
        break
    while current>s:
        win_size = i - left +1
        max1 = min(win_size,max1)
        current-=arr[left]
        left+=1
print(arr[start:end+1])