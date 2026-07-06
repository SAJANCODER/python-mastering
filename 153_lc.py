class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums)-1
        while start<end:
            mid = (start+end)//2
            if nums[mid] > nums[end]:
                start = mid +1    #why start here is , since the minimum is in right . we need to move forward toward right . so we using start = mid +1.
            else:
                end = mid
        return start
obj = Solution()
print(obj.findMin([3,4,5,1,2]))

