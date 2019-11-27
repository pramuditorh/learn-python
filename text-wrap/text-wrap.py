import textwrap

def wrap(string, max_width):
    s = '\n'.join(textwrap.wrap(string, max_width))
    return s

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)