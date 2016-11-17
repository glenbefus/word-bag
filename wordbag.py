#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import sys


class WordBag:
    def __init__(self):
        with open("/usr/share/dict/words", "r") as f:
            self._word_dictionary = frozenset(f.read().splitlines())

    def find_words_from_string_letters(self, bag_of_chars):
        letters = self._str_to_list(bag_of_chars)

        # TODO remove single character
        perms = set(self._get_permutations([""], letters))

        found_words = self._word_dictionary.intersection(perms)

        # TODO: format output
        print(str(found_words))

    def _get_permutations(self, list_curr_permutations, list_remaining_letters):
        if not list_remaining_letters:
            return list_curr_permutations

        results = []
        for letter in list_remaining_letters:
            sub_results = []
            for perm in list_curr_permutations:
                sub_results.append(perm + letter)

            rest_of_letters = list(list_remaining_letters)
            rest_of_letters.remove(letter)

            results += self._get_permutations(sub_results, rest_of_letters)

        return list_curr_permutations + results

    @staticmethod
    def _str_to_list(strng):
        char_list = []
        for c in strng:
            char_list.append(c)

        return char_list


def main(args):
    if len(args) != 2:
        print("Only one argument allowed.")
        return

    wordbag = WordBag()
    wordbag.find_words_from_string_letters(args[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv))
