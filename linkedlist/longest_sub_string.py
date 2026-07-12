#longest sub string
a = input("Enter a sring:").strip()
left = 0
seen= set()
max1 = 0
start = 0
for right in range(len(a)):
    while a[right] in seen:
        
        seen.remove(a[left])
        left+=1
    seen.add(a[right])
    current_window = right-left+1
    if current_window>max1:
        max1=current_window
        start=left
print(max1)
print("Substring is :",a[start:start+max1])