# nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
nums = [4,5,6,7,0,1,2]
target = 8
def find(nums,target):
    i = 0
    while i<len(nums):
        if nums[i] == target:
            return i
        else:
            i+=1
    return -1
    
print(find(nums,target))
