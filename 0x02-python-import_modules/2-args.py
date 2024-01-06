#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    iterable = sys.argv
    iterable = iterable[1:]

    def enumerate(iterable, start=1):
        n = start
        if len(sys.argv)-1 == 1:
            print('{} argument:'.format(len(sys.argv)-1))
        else:
            print('{} arguments:'.format(len(sys.argv)-1))
            for elem in iterable:
                print('{}: {}'.format(n, elem), end='\n')
                n += 1

    enumerate(iterable)
