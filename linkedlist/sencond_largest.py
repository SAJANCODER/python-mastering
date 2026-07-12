arr_in = list(map(int,input("Enter the array:").split()))

max1=arr_in[0]
second_max = 0
for i in range(len(arr_in)):
    if arr_in[i]>max1:
        second_max = max1
        max1=arr_in[i]
    elif arr_in[i]>second_max and arr_in[i]!=max1:
        second_max=arr_in[i]

print(second_max)