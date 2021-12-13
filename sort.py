#!/usr/bin/env python


import sys


if not sys.stdin.isatty():
    input_inf = sys.stdin
    for line in input_inf:
        line = sorted(line)
        sys.stdout.writelines(line)
        sys.stdout.write('\n')
else:
    try:
        input_filename = sys.argv[1]
    except IndexError:
        raise IndexError("Please, type name of the file")
    else:
        with open(sys.argv[1], 'r') as file:
            sorted_file = sorted(file)
        sys.stdout.writelines(sorted_file)
        sys.stdout.write('\n')
