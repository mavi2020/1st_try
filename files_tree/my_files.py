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


import glob

lst = []
sub_lst = []


# chld_lst = []

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


def get_childs(p_lst: list):
    for i in range(len(p_lst)):
        for j in range(len(p_lst)):
            if p_lst[i][1] == p_lst[j][0]:
                p_lst[i][3] = p_lst[j][0]
                print(i, j)
    return lst


get_parents('./files/*.txt')
child_lst = get_childs(lst)
print(lst)
