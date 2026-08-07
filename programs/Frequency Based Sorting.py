arr = list(map(int,input("Enter the array elements: ").split(" ")))
freq = {}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
final_arr = []
x=sorted(freq)
for i in x:
    final_arr.extend([i] * freq[i])

print(final_arr)