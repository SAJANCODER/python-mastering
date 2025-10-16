#Rotate a list in both directions (left and right) without using slicing (use loops instead).
num = list(map(int,input("Enter the list:").split()))
k = int(input("enter how many time to rotate using k value: "))
n = len(num)
left_rotate = num.copy()
right_rotate = num.copy()
# k = k%n #handle [1,2,3,4,5] if k(user swap value) =7 , then 7%5 =2
for i in range (k):
    left_shift = left_rotate.pop(0)
    left_rotate.append(left_shift)
    #right rotate
    right_shift = right_rotate.pop(-1)
    right_rotate.insert(0,right_shift)
print(f"Left Rotate: {left_rotate}")
print(f"Right Rotate: {right_rotate}")
