# n = input()
# ll = []
# left = 0
# for i in range(len(n)):
#     if n[i] in ll:
#         ll.append(n[i])
#         reverse = "".join(map(str,ll[::-1]))
#         if reverse == n[left:i+1]:
#             print(reverse)
            
#         else:
#             del ll[left]
#             left+=1
#             reverse1 = "".join(map(str,ll[::-1]))
#             if reverse1 == n[left:i+1]:
#                 print(reverse1)
                
#     else:
#         ll.append(n[i])

s = input()
left = 0
right = 2
max1 = 0 
fia = ""
start = 0
for i in range(len(s)):
        if len(s)==1:
            print(s)
   
        left = i
        right = i
        while left>=0 and right<len(s) and s[left] == s[right]:
            x = s[left:right+1]
            if len(x)>max1:
                max1 = len(x)
                start = left
            left-=1
            right+=1
   
        left = i
        right = i+1
        while left>=0 and right<len(s) and s[left] == s[right]:
                    x = s[left:right+1]
                    if len(x)>max1:
                        max1 = len(x)
                        start = left
                    left-=1
                    right+=1
print(max1)
print(s[start:start+max1])