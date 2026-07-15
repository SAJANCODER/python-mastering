#Given an array of positive integers and a target integer S, find the minimal length of a contiguous subarray of which the sum is greater S. If there isn't one, return 0.
arr = list(map(int,input("Enter the array:").split())) #1 5 5 6 7 2
target = 10
postion_arr = 0
current = 0
start=0
end=0
min_size = float('inf')
for i in range(len(arr)):
    current+=arr[i]
    if current>target:
        window_size = i - postion_arr +1
        min_size = min(min_size,window_size)
        start = postion_arr
        end = i
        current-=arr[postion_arr]
        postion_arr+=1
        print(arr[current:i])
if min_size==float('inf'):
    print(0)
else:
    print(min_size)
    print(arr[start:end+1])
    
