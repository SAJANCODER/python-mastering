version1 = input("Enter version 1:")
version2 = input("Enter version 2:")
# arr1 = []
# arr2 = []
# for i in version1:
#     if i!='0':
#         arr1.append(i)
# for j in version2:
#     if j!='0':
#         arr2.append(j)

# x = ("".join(arr1))
# y=("".join(arr2))

# if x>y:
#     print("1")
# elif x<y:
#     print("-1")
# else:
#     print("0")
v1 = version1.split(".")
v2 = version2.split(".")
length = max(len(v1),len(v2))
for i in range(length):
    if i<len(v1):
        num1 = int(v1[i])
    else:
        num1 = 0
    if i<len(v2):
        num2 = int(v2[i])
    else:
        num2=0
    if num1>num2:
        print("1")
        break
    elif num1<num2:
        print("-1")
        break
else:
    print("0")