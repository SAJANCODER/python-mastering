class Solution(object):
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums)-1
        while start<=end:
            mid_index = (start+end)//2
            if nums[mid_index] == target:
                return mid_index
            if nums[mid_index] > target:
                end = mid_index -1
            else:
                start = mid_index+1
        
        if nums[mid_index]>target:
            
            return mid_index
        else:
            
            return mid_index

nums = [1,3,5,6]
target = 4
obj = Solution()
print(obj.searchInsert(nums,target))