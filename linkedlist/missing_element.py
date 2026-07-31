arr = list(map(int,input("Enter the array elements:").split(" ")))
x = arr.sort()
actual_len = arr[-1]
# start = arr[0]
new_arr=[]
if len(arr)==1:
	new_arr.append(1)
for i in range(0,actual_len):
	if i not in arr:
		new_arr.append(i)
final_new = arr+new_arr
print("missing numbers are :",new_arr)
print(sorted(final_new))
	