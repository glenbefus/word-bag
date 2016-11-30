#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import math
import sys
from argparse import ArgumentParser
from argparse import FileType
from datetime import datetime


class WordBag(object):
    _word_dictionary = None

    def __init__(self):
        self._load_words_dictionary()
        self._permutation_cache = {}

    def find_words_from_string_letters(self, bag_of_chars):
        letters = list(filter(lambda x: x.isalpha(), iter(bag_of_chars)))

        possible_words = self._get_possible_words(letters)

        found_words_set = WordBag._word_dictionary.intersection(possible_words)

        self._print_words(found_words_set)

    def _get_possible_words(self, letters):
        all_combinations = self._get_power_set(letters)
        permutations = []
        for combo in all_combinations:
            permutations += self._get_same_length_permutations(combo)

        return frozenset(permutations)

    def _get_same_length_permutations(self, word):
        if len(word) <= 1:
            return [word]

        key = "".join(sorted(word))
        cached = self._permutation_cache.get(key, None)
        if cached:
            return cached

        word_list = list(word)

        results = []

        for index in range(0, len(word_list)):
            letter = word_list[index]
            other_letters = "".join(word_list[0:index] + word_list[index + 1:])
            permutations = self._get_same_length_permutations(other_letters)

            for perm in permutations:
                perm_list = list(iter(perm))
                perm_list.insert(0, letter)
                results.append("".join(perm_list))

        self._permutation_cache[key] = results
        return results

    @staticmethod
    def _get_power_set(char_list):
        results = []

        #  when the ith selected_set is 1, the ith char in char_list is in the set
        char_list_length = len(char_list)
        selected_set = int(math.pow(2, char_list_length) - 1)

        while selected_set > 0:
            combo = ""
            for i in range(0, char_list_length):
                bit_mask = 1 << i
                if (selected_set & bit_mask) > 0:
                    combo += char_list[char_list_length - 1 - i]

            results.append(combo)
            selected_set -= 1

        return results

    @staticmethod
    def _load_words_dictionary():
        if not WordBag._word_dictionary:
            with open("/usr/share/dict/words", "r") as f:
                WordBag._word_dictionary = frozenset(f.read().splitlines())

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

        find_words(letters)

        end = datetime.now()

        delta = end - start
        print("\nFound words in {0}".format(delta))
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


def find_words(letters):
    wordbag = WordBag()
    wordbag.find_words_from_string_letters(letters)


if __name__ == '__main__':
    sys.exit(main())
