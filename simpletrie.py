from enum import Enum


class SimpleTrieNode(object):
    def __init__(self):
        self._children = {}
        self._word = False

    def get_child_at_char(self, c):
        return self._children.get(c, None)

    def add_child_at_char(self, c):
        node = SimpleTrieNode()
        self._children[c] = node
        return node

    def is_word(self):
        return self._word

    def set_is_word(self, word):
        self._word = word


class FindWordResult(Enum):
    miss = 1
    prefix = 2
    word = 3


class SimpleTrie(object):
    def __init__(self):
        self._root = SimpleTrieNode()

    def add_word(self, word):
        curr_node = self._root

        for char in word:
            child = curr_node.get_child_at_char(char)
            if not child:
                child = curr_node.add_child_at_char(char)
            curr_node = child

        curr_node.set_is_word(True)

    def find_word(self, word):
        curr_node = self._root

        for char in word:
            child = curr_node.get_child_at_char(char)
            if not child:
                return FindWordResult.miss
            curr_node = child

        if curr_node.is_word():
            return FindWordResult.word

        return FindWordResult.prefix
