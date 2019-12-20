import string

alphabet = string.ascii_lowercase

def print_rangoli(size):
    addToList = []

    for i in range(size):
        s = "-".join(alphabet[i:size])
        addToList.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))

    print("\n".join(addToList[:0:-1] + addToList))

n = int(input())
print_rangoli(n)