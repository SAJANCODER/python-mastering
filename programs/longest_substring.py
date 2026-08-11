x = input()
left = 0

max = 0
seen = set()
start = 0
for i in range(len(x)):
    while x[i] in seen:
        seen.remove(x[left])
        left+= 1
    seen.add(x[i])
    current_window = len(seen)
    if current_window>max:
        max = current_window
        start = left
        
print(max)
print(left)
print(f"substring: ",x[left:left+max])
