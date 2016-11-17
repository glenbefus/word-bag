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

    letters = str_to_list(args[1])

    #TODO remove single character
    perms = set(get_permuations([""], letters))

    with open("/usr/share/dict/words", "r") as f:
        word_dictionary = frozenset(f.read().splitlines())
        found_words = word_dictionary.intersection(perms)

        #TODO: format output
        print(str(found_words))

def get_permuations(list_curr_permutations, list_remaining_letters):
    if not list_remaining_letters:
        return list_curr_permutations

    results = []
    for letter in list_remaining_letters:
        sub_results = []
        for perm in list_curr_permutations:
            sub_results.append(perm + letter)

        rest_of_letters = list(list_remaining_letters)
        rest_of_letters.remove(letter)

        results += get_permuations(sub_results, rest_of_letters)

    return list_curr_permutations + results

def str_to_list(str):
    list = []
    for c in str:
        list.append(c)

    return list

if __name__ == '__main__':
    sys.exit(main(sys.argv))