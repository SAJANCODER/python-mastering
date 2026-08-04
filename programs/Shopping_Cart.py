cans = int(input("Enter required cans: "))
pack_2 = int(input("Enter price of pack 2: "))
pack_4 = int(input("Enter price of pack 4: "))
minimum_cost = float('inf')
for i in range((cans//4)+1):
    for j in range((cans//2),0,-1):
        total_cans = (i*4) + (j*2)
        print(f"{i}+{j} = {total_cans}")
        if total_cans>=cans:
            cost = (i*pack_4) + (j*pack_2)
            minimum_cost= min(minimum_cost,cost)
print(minimum_cost)