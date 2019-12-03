n = input()

for i in n[:].split():
    n = n.replace(i, i.replace())

print(n)