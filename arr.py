arr = list(map(int,input("Enter the arr:").split(" ")))
inp = input("Enter your choice:")
if inp.lower() == "right":
    for i in range(len(arr)):
        right_rotate = arr[1:]+arr[:1]
        print(right_rotate)
elif inp.lower()=="left":
    for j in range(len(arr)):
        left_rotate = arr[:] + arr[:1]
        print(left_rotaten)

