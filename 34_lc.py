class Solution(object):
    def searchRange(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return[i]
           
        return[-1,-1]
if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    target = 8
    obj = Solution()
    print(obj.searchRange(nums,target))
