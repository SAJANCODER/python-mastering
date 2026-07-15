#Longest Substring Without Repeating Characters
a = input("Enter the string:")
left = 0
seen = set()
max1 = 0
for right in range(len(a)):
    while a[right] in seen:
        seen.remove(a[left])
        left+=1
    seen.add(a[right])
    current = right - left +1
    if current>max1:
        max1=current
        start = left
print(a[start:start+max1])


