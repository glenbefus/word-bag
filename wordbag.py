#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import sys
from datetime import datetime


class WordBag(object):
    _word_dictionary = None

    def __init__(self):
        self._load_words_dictionary()

    def find_words_from_string_letters(self, bag_of_chars):
        letters = self._str_to_list(bag_of_chars)

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

    @staticmethod
    def _str_to_list(string):
        char_list = []
        for c in string:
            char_list.append(c)

        return char_list


def main(args):
    if len(args) != 2:
        print("Only one argument allowed.")
        return

    start = datetime.now()
    wordbag = WordBag()
    wordbag.find_words_from_string_letters(args[1])
    end = datetime.now()

    print("\nFound words in {0} seconds".format((end - start).seconds))


if __name__ == '__main__':
    sys.exit(main(sys.argv))
