#!/usr/bin/env python


import sys
import argparse


def count_lines(input_inf):
    lines = 0
    for line in input_inf:
        lines += 1
    sys.stdout.write(str(lines))


def count_words(input_inf):
    words = 0
    for line in input_inf:
        words += len(line.split(" "))
    sys.stdout.write(str(words))


def count_bytes(input_inf):
    sys.stdout.write(sys.getsizeof(input_inf))


parser = argparse.ArgumentParser(description="It will help to analyze your text")
parser.add_argument("-l", "--lines", action='store_true', help="Print the number of rows in the object")
parser.add_argument("-w", "--words", action='store_true', help="Print the number of words in an object")
parser.add_argument("-c", "--bytes", action='store_true', help="Print the size of the object in bytes")
parser.add_argument("input", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
args = parser.parse_args()


with args.input as input_inf:
    if args.lines:
        count_lines(input_inf)
    elif args.words:
        count_words(input_inf)
    elif args.bytes:
        count_bytes(input_inf)
    elif args.lines and args.words:
        count_lines(input_inf)
        count_words(input_inf)
    elif args.lines and args.bytes:
        count_lines(input_inf)
        count_bytes(input_inf)
    elif args.words and args.bytes:
        count_words(input_inf)
        count_bytes(input_inf)
    else:
        count_lines(input_inf)
        count_words(input_inf)
        count_bytes(input_inf)
