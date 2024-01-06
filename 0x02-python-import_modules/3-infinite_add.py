#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    iterable = sys.argv
    iterable = iterable[1:]
    new_list = []

    for elem in iterable:
        elem_int = int(elem)
        new_list.append(elem_int)
    print(sum(new_list))
