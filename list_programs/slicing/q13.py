#For a given list, perform rotation until it comes back to the original arrangement. Count the number of rotations needed.
lst = list(map(int,input("Enter a list:").split()))
k = int(input("Enter the rotation: "))
n=len(lst)

def count_rotation(lst,k,n):
    k = k%n
    org = lst[:]
    mirror = lst[:]
    count = 0
    while True:
        mirror = mirror[-k:] + mirror[:-k]
        count+=1
        if mirror == org:
            return count

print(f"Rotation for the list {lst} , is come back to orginal after {count_rotation(lst,k,n)}")
