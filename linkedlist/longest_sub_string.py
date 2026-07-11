#longest sub string
a = input("Enter the string: ").split()
seen = []
for i in a :
    print(seen)
    if i in seen:
        seen.remove(i)
        seen.append(i)
    else:
        seen.append(i)
print(len(seen))