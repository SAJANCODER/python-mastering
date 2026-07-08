a=list(map(int,input().split()))
# b=int("".join(map(str,a)))
target = 10
hash={}
for index,value in enumerate(a):
    num = target-value
    hash[value] = index
    if num in hash:
        print(hash[value])
