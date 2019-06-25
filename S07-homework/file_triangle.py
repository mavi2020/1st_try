fr = open('input.txt')

n = int(fr.readline())
pattern = fr.readline()
fr.close()
fw = open('triangle.txt', mode='w')
i = 1
pattern_1 = 'p1\n'
while i <= n:
    white = " " * (n - i)
    stars = pattern * (2 * i - 1)
    pattern_1 = pattern_1 + white + stars + '\n'
    i = i + 1
fw.write(pattern_1)
# fw.close()

i = 1
pattern_2 = 'p2\n'
while i <= n:
    white = " " * (n - i)
    if i % 2 == 1:
        stars = pattern * (2 * i - 1)
    else:
        mid_whites = " " * (2 * i - 3)
        stars = pattern + mid_whites + pattern

    pattern_2 = pattern_2 + white + stars + '\n'
    i = i + 1
fw.write(pattern_2)

i = 1
pattern_3 = 'p3\n'
while i <= n:
    white = " " * (n - i)
    if i == 1:
        stars = pattern
    elif i == n:
        stars = pattern * (2 * i - 1)
    else:
        mid_whites = " " * (2 * i - 3)
        stars = pattern + mid_whites + pattern

    pattern_3 = pattern_3 + white + stars + '\n'
    i = i + 1
fw.write(pattern_3)
