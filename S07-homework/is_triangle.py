def extract_file(file):
    lines = file.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(',', '').split()
    return lines


def side(line):
    ls = []
    for i in range(len(line)):
        ls = lst.append(line[i])

    return ls


fr = open('inp.txt')

sides_lst = extract_file(fr.read())
side(sides_lst)

# lst.append(line_data)
lst = []
