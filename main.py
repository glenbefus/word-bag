#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#

import sys

def main(args):
    if len(args) != 2:
        print("Sorry, I only accept one argument.")
        return

    letters = args[1]

    print(letters)

    with open("/usr/share/dict/words", "r") as f:
        dictionary = set(f.read().splitlines())
        print(str(dictionary))

if __name__ == '__main__':
    sys.exit(main(sys.argv))