a = list(map(int,input().split()))
target = 10
hash={}
for index,value in enumerate(a):
    num = target-value
    if num in hash:
        print(hash[num],index)
    hash[value]=index