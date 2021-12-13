#!/usr/bin/env python


import os
import sys
import argparse


parser = argparse.ArgumentParser(description="Check the last lines in file")
parser.add_argument("input", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument("-n", help="Output the specified number of lines from the end of the file")
args = parser.parse_args()

with args.input as input_inf:
    if args.n:
        num = int(args.n)
        lines = input_inf.readlines()
        n_lines = lines[-num:]
        for line in n_lines:
            sys.stdout.writelines(line)
    else:
        lines = input_inf.readlines()
        n_lines = lines[-10:]
        for line in n_lines:
            sys.stdout.writelines(line)
