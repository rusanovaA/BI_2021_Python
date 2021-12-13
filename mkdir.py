#!/usr/bin/env python

import os
import argparse


parser = argparse.ArgumentParser(description="Create a directory or directories")
parser.add_argument("dirname", type=str, help="Type name of new directory")
parser.add_argument("-p", action='store_true', help="Type the names of new directories")
args = parser.parse_args()

if args.p:
    os.makedirs(args.dirname)
else:
    os.mkdir(args.dirname)
