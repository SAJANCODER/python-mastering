arr = list(map(int,input("enter an array values:").split(" ")))
new_arr1 = arr[1:]
value = arr[:1]
int_val = int("".join(map(str,value)))
mul1=1
new_arr2 = []
for i in new_arr1:
    mul1*= i*int_val
new_arr2.append(mul1)
print(new_arr2+new_arr1)
