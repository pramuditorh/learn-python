d = {}
avg = 0

for _ in range(int(input())):
    n, *l = input().split()
    score = list(map(float, l))
    d[n] = score

query_name = input()
avg = sum(d[query_name])/len(d[query_name])

print("{0:.2f}".format(avg))