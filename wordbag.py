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
        self._permutation_cache = {}

    def find_words_from_characters(self, characters):
        letters = list(filter(lambda x: x.isalpha(), iter(characters)))

        found_words_set = frozenset(self._find_possible_words(letters))

        self._print_words(found_words_set)

        return len(found_words_set)

    def _find_possible_words(self, remaining, taken=""):
        if len(remaining) == 0:
            return []

        results = []

        for index in range(0, len(remaining)):
            letter = remaining[index]
            possible_word = taken + letter
            is_prefix = WordBag._dictionary_trie.find_word(possible_word)
            if is_prefix is None:
                continue
            elif not is_prefix:
                results.append(possible_word)

            results += self._find_possible_words(remaining[0:index] + remaining[index + 1:], possible_word)

        return results

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
        print("\nFound {1} words in {0}".format(delta, num_words_found))
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
