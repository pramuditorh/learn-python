n, m = [int (x) for x in input().split()]

l = [('.|.' * (2*i+1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(l + ['WELCOME'.center(m, '-')] + l[::-1]))