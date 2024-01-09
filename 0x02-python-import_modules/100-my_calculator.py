#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    import calculator_1

    iterable = sys.argv
    iterable = iterable[1:]

    def enumerate(iterable):
        if len(iterable) != 3:
            print('Usage: ./100-my_calculator.py <a> <operator> <b>')
            exit(1)
        else:
            a = int(iterable[0])
            b = int(iterable[2])
            if iterable[1] == '+':
                print('{} {} {} = {}'.format(iterable[0], iterable[1],
                iterable[2], calculator_1.add(a, b)))
            elif iterable[1] == '-':
                print('{} {} {} = {}'.format(iterable[0], iterable[1],
                iterable[2], calculator_1.sub(a, b)))
            elif iterable[1] == '*':
                print('{} {} {} = {}'.format(iterable[0], iterable[1],
                    iterable[2], calculator_1.mul(a, b)))
            elif iterable[1] == '/':
                print('{} {} {} = {}'.format(iterable[0], iterable[1],
            iterable[2], calculator_1.div(a, b)))
            else:
                print('Unknown operator. Available operators: +, -, * and /')
                exit(1)
    enumerate(iterable)
