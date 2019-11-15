n = int(input())
arr = list(map(int, input().split()))

arr = [x for x in arr if x != max(arr)]
arr.sort()
print(arr[-1])