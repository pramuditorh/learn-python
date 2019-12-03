def is_leap_year(year):
    leap = False

    if year % 4 == 0 and (year % 400 == 0 or year % 100 !=0):
        leap = True
    return leap

x = int(input())
print(is_leap_year(x))