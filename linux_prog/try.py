#Given a circular rotation, find the element at the kth index after n rotations.

lst = list(map(int,input("Enter a list: ").split()))
n = int(input("Enter how many rotation: "))
k = int(input("enter the index you need:"))
choice = input("Enter your choice (Left(L)/Right(R)) rotation: ")
right_rotate = lst.copy()
left_rotate = lst.copy()
for i in range(n):

        rotate_l = left_rotate[1:] + left_rotate[:1]
        left_rotate = rotate_l

        rotate_r = right_rotate[-1:] + right_rotate[:-1]
        right_rotate = rotate_r
if choice.upper() == 'L':
    print(f"Left Rotate : The value of k is {left_rotate[k]} , after {n} rotation")
elif choice.upper() == 'R':
    print(f"Right Rotate : The value of k is {right_rotate[k]} , after {n} rotation")
else:
    print("INVALID INPUT")