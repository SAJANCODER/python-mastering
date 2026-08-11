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
initial = 0
last = -1
final = ""
for i in range(len(s)):
    if s[initial]==s[last]:
        final = s[initial:last+1]
    else:
        last-=1
        initial+=1
print(final)