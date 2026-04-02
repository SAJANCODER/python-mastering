arr = [4,5,3,3,5]
target = 8 
hashmap = {}
for i, num in enumerate(arr):
	compliment = target - num
	if compliment in hashmap:
		print(hashmap[compliment],i)
	hashmap[num] =i

