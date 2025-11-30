#binary search 
arr = [1,2,3,4,5,6,7,8,9,10]
start = 0
end = len(arr) - 1
target = 10

def binary_search(arr,start,end,target):
    while start<=end:
        mid_index = (start+end)//2
        if arr[mid_index] == target :
            return True
        elif arr[mid_index] > target :
            end = mid_index -1
            
        else:
            start = mid_index +1
            
    return -1
print(binary_search(arr,start,end,target))
            
