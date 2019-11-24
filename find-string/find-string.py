import re

def count_substring(string, sub_string): 
    return len(re.findall(f'(?={sub_string})', string))

string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)