#Reverse word in an sentence"
a =input("Enter the sentence:").split()
result = []
for word in a:
	result.append(word[::-1])
print(" ".join(result))


