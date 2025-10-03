#Rotate a list to the right by k positions (user should enter k).
#Example: List = [1,2,3,4,5], k=3 → [3,4,5,1,2]
num = list(map(int,input("enter the list:").split()))
user = int(input("enter the k position for right rotate:"))
rotate = num[-user:] + num[:-user]
print(f"Right Rotate : {rotate}")