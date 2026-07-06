#Given an array of integers nums and an integer k, return the number of subarrays whose sum equals k. (Classic subarray sum equals K.)
nums = [1,2,3,4,5,6,7,8,9,10]
k = 10
subarry = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == k:
            subarry.append((nums[i],nums[j]))
            
print(subarry)