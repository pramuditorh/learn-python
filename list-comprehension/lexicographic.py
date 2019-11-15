x = int(input())
y = int(input())
z = int(input())
n = int(input())
'''
#Using for loops
ar = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            if i+j+k != n:
                ar.append([i, j, k])

print(f"w/o list comprehension {ar}")
'''
print(f"list comprehension{[[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(z+1) if i+j+k != n]}")