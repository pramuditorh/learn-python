m, n = list(map(int, input().split())) 
ar = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happines = 0

for i in ar:
    if i in A:
        happines += 1
    elif i in B:
        happines -= 1

print(happines)