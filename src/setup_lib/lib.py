from tabulate import tabulate

def get_table(last_name):
    table = [
            ['foo', 23, True],
            ['bar', 42, False],
            [last_name, -3,5, None]
            ]

    return tabulate(table)

if __name__ == '__main__':
    import sys
    print(get_table(sys.argv[1]))
