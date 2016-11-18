#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  wordbag.py
#

import sys


class WordBag:
    def __init__(self):
        self._two_letter_words = frozenset(["at", "it", "am"])
        with open("/usr/share/dict/words", "r") as f:
            self._word_dictionary = frozenset(f.read().splitlines())

    def find_words_from_string_letters(self, bag_of_chars):
        letters = self._str_to_list(bag_of_chars)

        perms = frozenset(self._get_permutations([""], letters))
        perms = filter(lambda x: len(x) > 2 or x.lower() in self._two_letter_words, perms)

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
    def _str_to_list(string):
        char_list = []
        for c in string:
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
