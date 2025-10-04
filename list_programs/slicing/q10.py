#Given a circular rotation, find the element at the kth index after n rotations.

num = list(map(int,input("Enter the list: ").split()))
print(num)
n_rotation = int(input("Enter how many Rotation you want to Perform: "))
k=int(input("Enter the Index Position you need after the n rotation: "))
new_list = num.copy()
for i in range(n_rotation):
    right_rotation = new_list[-1:] + new_list[:-1]
    new_list = right_rotation
print(f"After {n_rotation} rotation, The index value is {new_list[k]} ")

                    #OR method

num = list(map(int,input("Enter the list: ").split()))
print(num)
n_rotation = int(input("Enter how many Rotation you want to Perform: "))
k=int(input("Enter the Index Position you need after the n rotation: "))
choice = input("You need to perform Right Rotetaion(R) or Left Rotation(L): ").upper()[0]
if choice == 'R':
    right_rotation = (k- n_rotation)% len(num)
    print(f"After {n_rotation}, the index value for is {num[right_rotation]}")
elif choice=='L':
    left_rotation = (k+n_rotation)% len(num)
    print(f"After {n_rotation}, the index value for is {num[left_rotation]}")
else:
    print("INVALID INPUT")