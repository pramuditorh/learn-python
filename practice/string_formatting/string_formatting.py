def print_formatted(number):
    for i in range(1, number+1):
        print(f"{i}\t{oct(i).split('o')[-1]}\t{hex(i).split('x')[-1].capitalize()}\t{bin(i).split('b')[-1]}")

n = int(input())
print_formatted(n)