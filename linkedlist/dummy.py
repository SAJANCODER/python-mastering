print("\t\tFLAMES Program\n")

name1 = input("Enter name 1: ").replace(" ", "").upper()
name2 = input("Enter name 2: ").replace(" ", "").upper()

# Convert to lists
list1 = list(name1)
list2 = list(name2)

# Remove common letters
for ch in name1:
    if ch in list2:
        list1.remove(ch)
        list2.remove(ch)

count = len(list1) + len(list2)

print("Remaining count:", count)

flames = ["F", "L", "A", "M", "E", "S"]

while len(flames) > 1:
    index = (count) % len(flames)

    # Remove the letter
    flames.pop(index)

    # Rearrange list so counting continues from next position
    flames = flames[index:] + flames[:index]

result = flames[0]

meaning = {
    "F": "Friends",
    "L": "Love",
    "A": "Affection",
    "M": "Marriage",
    "E": "Enemies",
    "S": "Siblings"
}

print(f"Result: {meaning[result]}")
