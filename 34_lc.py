# class Solution(object):
#     def searchRange(self, nums, target):
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 return[i]
           
#         return[-1,-1]
# if __name__ == "__main__":
#     nums = [5,7,7,8,8,10]
#     target = 8
#     obj = Solution()
#     print(obj.searchRange(nums,target))
#Given a rotated sorted array nums (no duplicates) and an integer target, return the index of target if it exists, otherwise return -1.
#Rotation example: [4,5,6,7,0,1,2] is [0,1,2,4,5,6,7] rotated.

#We must do it in O(log n) time.

arr = [0,1,2,4,5,6,7]
target = 6

def find(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(find(arr,target))
        