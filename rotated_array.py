#before rotation:[4,5,6,7,0,1,2]
#after rotation: [0,1,2,4,5,6,7]

n = [4,5,6,7,0,1,2]

#right rotate
right_rotate = n[-3:] + n[:-3]
print(f"for {n} array is {right_rotate}")