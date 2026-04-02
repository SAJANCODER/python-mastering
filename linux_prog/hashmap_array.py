arr = [1,2,3,4,5]
target =7
hashmap = {}
for i,num in enumerate(arr):
	compliment = target - num
	if compliment in hashmap:
		print(hashmap[compliment],i)
		break
	hashmap[num] = i
