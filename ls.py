#!/usr/bin/env python

import os
import argparse


def dirs_fils(input_inf):
    with os.scandir() as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_dir():
                print(entry.name)
            if not entry.name.startswith('.') and entry.is_file():
                print(entry.name)


def all_dirs_fils(input_inf):
    with os.scandir() as it:
        for entry in it:
            if entry.is_dir():
                print(entry.name)
            if entry.is_file():
                print(entry.name)


parser = argparse.ArgumentParser(description="View folder contents")
parser.add_argument("path", type=str, default=".", help="Type the path to the desired folder")
parser.add_argument("-a", action='store_true', help="Display all files, including hidden ones")
args = parser.parse_args()

input_inf = args.path

if args.a:
    all_dirs_fils(input_inf)
else:
    dirs_fils(input_inf)
