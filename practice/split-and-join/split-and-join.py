def split_and_join(line): 
    line = line.split(" ")

    return '-'.join(line)

s = input()
result = split_and_join(s)
print(result)