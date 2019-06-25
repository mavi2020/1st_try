def fact(n):
    f = 1
    if n == 0:
        f = 1
    elif n >= 1:
        while n:
            f *= n
            n -= 1
    return f


def combination(m, n):
    val_1 = fact(m)
    val_2 = fact(n)
    val_3 = fact(m - n)
    c = val_1 / (val_2 * val_3)
    return int(c)


def pascal_row(row):
    lst = []
    for i in range(row + 1):
        lst.append(combination(row, i))
    return lst


def pascal(row):
    lst = []
    for i in range(row):
        lst.append(pascal_row(i))
    return lst


for line in pascal(12):
    print(line)
