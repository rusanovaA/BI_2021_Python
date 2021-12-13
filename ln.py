#!/usr/bin/env python


import os
import argparse


parser = argparse.ArgumentParser(description="Create hard and symbolic link")
parser.add_argument("target", type=str, help="Target")
parser.add_argument("link", type=str, help="Link")
parser.add_argument("-s", help="Create a symbolic link")
args = parser.parse_args()

if args.s:
    os.symlink(args.target, args.link)
else:
    os.link(args.target, args.link)
