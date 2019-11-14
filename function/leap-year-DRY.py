def is_leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

x = int(input())
print(is_leap_year(x))


"""
DRY - Dont Repeat Yourself
"""