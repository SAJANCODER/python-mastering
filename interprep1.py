stra = input("Enter the input:")
seen = set()
duplicate = set()
for c in stra:
	if c in seen:
		duplicate.add(c)
	else:
		seen.add(c)
for c in stra:
	if c not in duplicate:
		print(c)
		break

		
#method 2
s = input("Enter a String:")
for c in s:
	if s.count(c) == 1:
		print(c)
		break
	
