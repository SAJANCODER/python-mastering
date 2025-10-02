num = list(map(int,input("enter the list:").split()))
left_rotate = num[1:] + num[:1]
print(f"Left Rotate:{left_rotate}")
right_rotate = num[-1:] +num[:-1]
print(f"Right Rotate:{right_rotate}")