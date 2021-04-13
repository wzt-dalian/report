import os
import sys

rootdir = 'C:\\Users\\username2\\Desktop\\Tri_area'


def print_dict(input):
    for k, v in input.items():
        print(k, v, sep=":")


def listAllFiles(rootPath, mlist):
    list = os.listdir(rootPath)
    for i in range(0, len(list)):
        path = os.path.join(rootPath, list[i])
        if os.path.isfile(path):
            mlist.append(path)
        elif os.path.isdir(path):
            listAllFiles(path, mlist)


if __name__ == "__main__":
    mylist = []
    listAllFiles(rootdir, mylist)
    print(*[x for x in mylist], sep="\n")
    print(len(mylist))

    print(sys.path)
    print_dict({x: x ** 3 for x in range(4)})

    print(sys.builtin_module_names, dir(__builtins__))
