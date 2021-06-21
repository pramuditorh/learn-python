'''
Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem
'''

def diagonal_difference(arr):
    sum1 = 0
    sum2 = 0
    diff = 0
    l = len(arr)
    for i in range(l):
        for j in range(l):
            if i == j:
                sum1 += arr[i][j]
            #if (j - i) == (l-i-1):
        sum2 += arr[i][l-i-1]

    diff = abs(sum1 - sum2)

    return diff

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

print(diagonal_difference(arr))