def ms(s, p, c):
    s = list(s)
    s[p] = c
    s = ''.join(s)
    return s

string = input()
pos, char = input().split()

print(ms(string, int(pos), char))