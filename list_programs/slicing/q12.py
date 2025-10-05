#Use list comprehension to rotate a list by k positions.
num = list(map(int,input("Enter a list: ").split()))
k = int(input("Enter the rotation:"))
n=len(num)
#list comprehension
rotate = [num[(i+k)%n] for i in range(n)]
print(f"Left Rotate: {rotate}")