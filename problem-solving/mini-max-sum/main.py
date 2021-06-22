def miniMaxSum(arr):
    minMaxSum = []
    temp = 0
    for i in range(len(arr)):
        sum = 0
        temp = arr.pop(i)
        for j in range(len(arr)):
            sum += arr[j]
        minMaxSum.append(sum)
        arr.insert(i, temp)
    
    return f'{min(minMaxSum)} {max(minMaxSum)}'

arr = list(map(int, input().rstrip().split()))
print(miniMaxSum(arr))