n = int(input())
m = [[input(), float(input())] for _ in range(n)]

x = sorted(m, key = lambda val: val[1])[1][1]

for k, l in m:
    if l == x:
        print(k)