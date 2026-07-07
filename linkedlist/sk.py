s=int(input())
lst = []
for i in range(s):
    val=list(map(int,input().split()))
    lst.append(val)
sum1=0
for i in range(s):
    sum1+=lst[i][i]
    sum1+=lst[i][s-1-i]
if s%2==1:
    sum1-= lst[s//2][s//2]
print(sum1)
