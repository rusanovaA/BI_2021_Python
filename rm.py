#!/usr/bin/env python

import os
import shutil
import argparse


parser = argparse.ArgumentParser(description="Delete file or directory")
parser.add_argument("filename", type=str, help="Type the file name")
parser.add_argument("-r", action='store_true', help="Type the name of directory")
args = parser.parse_args()

if args.r:
    shutil.rmtree(args.filename)
else:
    os.remove(args.filename)
