def merge_the_tools(string, k):
    for i in range(int(len(string)/k)):
        output = ''
        for j in string[i * k:(i + 1) * k]:
            if j in output:
                continue
            output += j
        print(output)
        
string, k = input(), int(input())
merge_the_tools(string, k)