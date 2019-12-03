n, m = [int (x) for x in input().split()]

l = []

for i in range(n // 2):
    l.append(('.|.' * (2*i+1)).center(m, '-'))

s = '\n'.join(l)
print(s + '\n' + 'WELCOME'.center(m, '-') + '\n' + '\n'.join(l[::-1]))