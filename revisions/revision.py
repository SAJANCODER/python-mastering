
# For a given list, perform rotation until it comes back to the original arrangement. Count the number of rotations needed. --completed



lst = list(map(int,input("Enter a list: ").split()))
n = len(lst)
original_list = lst.copy()
mirror_list = lst.copy()
count = 0
while True:
    mirror_list = mirror_list[1:]+mirror_list[:1]
    count+=1
    if original_list == mirror_list:
        break
print(f"List {lst}, after n rotation it return back to original position at count {count} ")
