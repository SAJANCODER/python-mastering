# remove duplicate in string
a = input("Enter a String:")
result = ""
for i in a :
	if i not in result:
		result+=i
print(result)
