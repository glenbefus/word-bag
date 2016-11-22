#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import sys
from argparse import ArgumentParser
from datetime import datetime


class WordBag(object):
    _word_dictionary = None

    def __init__(self):
        self._load_words_dictionary()

    def find_words_from_string_letters(self, bag_of_chars):
        letters = list(filter(lambda x: x.isalpha(), iter(bag_of_chars)))

        possible_words = self._get_possible_words(letters)

        found_words_set = WordBag._word_dictionary.intersection(possible_words)

        self._print_words(found_words_set)

    def _get_possible_words(self, letters):
        return frozenset(self._get_permutations([""], letters))

    def _get_permutations(self, list_curr_permutations, list_remaining_letters):
        if not list_remaining_letters:
            return list_curr_permutations

        results = []
        for letter in list_remaining_letters:
            results_set = frozenset(results)
            sub_results = []
            for perm in list_curr_permutations:
                next_perm = perm + letter
                if next_perm in results_set:
                    continue

                sub_results.append(next_perm)

            rest_of_letters = list(list_remaining_letters)
            rest_of_letters.remove(letter)

            results += self._get_permutations(sub_results, rest_of_letters)

        return list_curr_permutations + results

    @staticmethod
    def _load_words_dictionary():
        if not WordBag._word_dictionary:
            with open("/usr/share/dict/words", "r") as f:
                WordBag._word_dictionary = frozenset(f.read().splitlines())

    @staticmethod
    def _print_words(found_words):
        found_words_list = list(found_words)
        found_words_list.sort()
        for word in found_words_list:
            print(word)


def main():
    parser = ArgumentParser()
    parser.add_argument("letters", help="list of letters")
    parser.add_argument("-b", "--benchmark", action="store_true",
                        help="print how long the program ran for")

    args = parser.parse_args()

    letters = args.letters

    if args.benchmark:
        start = datetime.now()

        find_words(letters)

        end = datetime.now()
        print("\nFound words in {0} milliseconds".format((end - start).microseconds / 1000))
    else:
        find_words(letters)


def find_words(letters):
    wordbag = WordBag()
    wordbag.find_words_from_string_letters(letters)


if __name__ == '__main__':
    sys.exit(main())
