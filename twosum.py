class Solutions:
    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

nums = [1,2,3,4]
target = 7
x=Solutions()
print(x.twosum(nums,target))
