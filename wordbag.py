#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import sys
from argparse import ArgumentParser
from argparse import FileType
from datetime import datetime

from simpletrie import SimpleTrie


class WordBag(object):
    _dictionary_trie = None

    def __init__(self):
        self._load_dictionary()

    def find_words_from_characters(self, characters):
        letters = list(filter(lambda x: x.isalpha(), iter(characters)))
        found_words_set = frozenset(self._find_possible_words(letters))
        self._print_words(found_words_set)
        return len(found_words_set)

    @staticmethod
    def _find_possible_words(letters):
        return WordBag._dictionary_trie.find_possible_words(letters)

    @staticmethod
    def _load_dictionary():
        if not WordBag._dictionary_trie:
            with open("/usr/share/dict/words", "r") as f:
                WordBag._dictionary_trie = SimpleTrie()
                for line in f.read().splitlines():
                    WordBag._dictionary_trie.add_word(line)

    @staticmethod
    def _print_words(found_words):
        for word in sorted(found_words):
            print(word)


def main():
    args = parse_arguments()

    letters = args.letters
    if not letters:
        for line in args.infile:
            letters += line

    if args.benchmark:
        start = datetime.now()
        num_words_found = find_words(letters)
        end = datetime.now()

        delta = end - start
        print("\nFound {0} words in {1}".format(num_words_found, delta))
    else:
        find_words(letters)


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument("infile", nargs="?", type=FileType("r"), default=sys.stdin,
                        help="file name for input, default is stdin")
    parser.add_argument("outfile", nargs="?", type=FileType("w"), default=sys.stdout,
                        help="file name for output, default is stdout")
    parser.add_argument("-l", "--letters", help="list of letters, alternative to infile", default="", )
    parser.add_argument("-b", "--benchmark", action="store_true",
                        help="print how long the program ran for")
    return parser.parse_args()


def find_words(characters):
    word_bag = WordBag()
    return word_bag.find_words_from_characters(characters)


if __name__ == '__main__':
    sys.exit(main())
