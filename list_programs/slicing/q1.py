#Write a program to rotate a list to the left by one position.
#Example: [1,2,3,4,5] → [2,3,4,5,1]

num = list(map(int,input("enter the list:").split()))
left_rotate = num[1:] + num[:1]
print("Left Rotate: ",left_rotate)