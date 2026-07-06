#Given a rotated sorted array nums (no duplicates) and an integer target, return the index of target if it exists, otherwise return -1.
#Rotation example: [4,5,6,7,0,1,2] is [0,1,2,4,5,6,7] rotated.

#We must do it in O(log n) time.

arr = [0,1,2,4,5,6,7]
target = 6
start = 0
end = len(arr) -1
def log_n(arr,start,target,end):
    while start<=end:

        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]>target:
            end = mid-1
        else:
            start = mid+1
    return start
print(log_n(arr,start,target,end))
        