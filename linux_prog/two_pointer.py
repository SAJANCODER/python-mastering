arr = [1,3,4,5,7,10]
target = 9
left = 0
right = len(arr)-1
for i in range(len(arr)-1):
	sum = arr[left]+arr[right] 
	if sum==target:
		print(left,right)
	elif sum>target:
		right-=1
	elif sum<target:
		left+=1

