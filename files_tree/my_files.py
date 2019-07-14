class Node:
    chld_lst = []

    def __init__(self, data):
        self.data = data
        self.file_name = ""
        self.parent = False

    def set_filename(self, name):
        self.file_name = name
        return self

    def set_parent(self):
        self.parent = True
        return self

    def set_child(self, chld_name):
        self.chld_lst.append(chld_name)
        return self


def get_parents(path):
    list_of_files = glob.glob(path)
    for f in list_of_files:
        d = open(f)
        d = d.read()
        s = f.split("\\")
        ss = s[1].split(".txt")
        if int(d) == 0:
            lst.append([ss[0], d, True, []])
        else:
            lst.append([ss[0], d, False, []])
    return lst


def get_child(lst):
    tmp = []
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            a = lst[i][0]
            b = lst[j + 1][1]
            if a == b:
                tmp.append(lst[j + 1][0])
                print(i, j)
        lst[i][3] = tmp
        tmp = []
    return lst


def get_leaf(lst):
    f = open('no_child.txt', mode='w')
    for i in range(len(lst)):
        if len(lst[i][3]) == 0:
            f.write(lst[i][0])
    f.close()
    return 0


import glob

lst = []
sub_lst = []

get_parents('./files/*.txt')
print(lst)
