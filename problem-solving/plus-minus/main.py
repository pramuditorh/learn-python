def plusMinus(arr, n):
    positive = 0
    minus = 0
    zero = 0
    
    for i in arr:
        if i < 0:
            minus += 1 
        elif i > 0:
            positive += 1
        else:
            zero += 1
    print("{0:.6f}".format(positive/n, 6))
    print("{0:.6f}".format(minus/n, 6))
    print("{0:.6f}".format(zero/n, 6))

n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

plusMinus(arr, n)