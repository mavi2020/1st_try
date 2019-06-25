lst = [4, 2, 59, 32]
print(lst)
length = len(lst)

for j in range(length):
    for i in range(length - 1):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(lst)
