N = int(input())
n = input().split()

for i in range(N):
    tup = [int(x) for x in n]
tup = hash(tuple(tup))
print(tup)