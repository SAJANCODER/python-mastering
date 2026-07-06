# Given a sorted array and a target, return the index of the target OR -1 if not found.

# Example:

# nums = [-1,0,3,5,9,12]
# target = 9
# Output: 4
nums = [-1,0,3,5,9,12]
target = 9

start=0
end=len(nums)-1
def binary_search(nums,target,start,end):
    while start<=end:
        
        mid_index = (start+end)//2
        
        if nums[mid_index] == target:
            return mid_index
        if nums[mid_index]>target:
            end = mid_index - 1
        else:
            start = mid_index + 1
print(binary_search(nums,target,start,end))
    
