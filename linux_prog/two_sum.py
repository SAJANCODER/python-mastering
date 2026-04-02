print("We are Solving this two sum in 2 approach ;\n one is with O(n2) and another is O(n)")
a=int(input("Enter 1 or 2 to procceed: "))
if a== 1:
	arr = [2,7,11,15]
	target = 9
	for i in range(len(arr)):
		for j in range(i+1,len(arr)):
			if arr[i]+arr[j] == target:
				print(i,j)
elif a==2:
	arr = [2,7,11,15]
	target = 9
	hashmap={}
	for i,num in enumerate(arr):
		values = target-num
		if values in hashmap:
			print(hashmap[values],i)
		hashmap[num]=i
else:
	print("Enter a valid input")
