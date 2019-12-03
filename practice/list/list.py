l = []
for _ in range(int(input())):
    x = input().split()
    arg = x[1:]
    m = x[0]
    if m == 'print':
        print(l)
    else:
        m  = ''.join(m)+f"({', '.join(arg)})"
        eval(f"l.{m}")