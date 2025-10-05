#Implement a function rotate_list(lst, k, direction) where direction can be "left" or "right".

lst = list(map(int,input("Enter the list:").split()))
k = int(input("Enter the how many rotation :"))
direction = input("Enter the direction: ")

def rotate_list(lst,k,direction):
    if not lst:
        return lst
    if direction.lower() == "right":
        rotate = lst[-k:] + lst[:-k]
    elif direction.lower() == "left":
        rotate = lst[k:] + lst[:k]
    return rotate
if direction.lower() == "left":
    print("Left rotate: ",rotate_list(lst,k,direction))
else:
    print("Right rotate: ", rotate_list(lst, k, direction))


