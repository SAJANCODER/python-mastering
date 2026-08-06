# arr = list(map(int,input("Enter the array:").split(" ")))
# even = []
# odd = []
# eve_pos = []
# odd_pos = []
# for i in range(len(arr)):
#     if arr[i]%2!=0:
#         odd.append(arr[i])
#         odd_pos.append(i)
#     elif arr[i]%2==0:
#         even.append(arr[i])
#         eve_pos.append(i)
# eve_sort = sorted(even,reverse=True)
# merged = arr.copy()
# final_arr = []
# odd_pointer = 0
# even_pointer = 0
# for i in range(len(merged)):
#     if merged[i] in odd:
#         final_arr.append(odd[odd_pointer])
#         odd_pointer+=1
#     elif merged[i] in even:
#         final_arr.append(eve_sort[even_pointer])
#         even_pointer+=1
# print(final_arr)

#approach 2

arr = list(map(int,input("Enter the array:").split(" ")))
even_arr = []
odd_arr = []
for i in arr:
    if i%2!=0:
        odd_arr.append(i)
    elif i%2==0:
        even_arr.append(i)
odd_sorted = sorted(odd_arr)
even_sorted = sorted(even_arr,reverse=True)
e=0
o=0
final_arr = []
for i in arr:
    if i%2!=0:
        final_arr.append(odd_sorted[o])
        o+=1
    elif i%2==0:
        final_arr.append(even_sorted[e])
        e+=1
print(final_arr)