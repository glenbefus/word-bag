class SimpleTrieNode(object):
    def __init__(self):
        self._children = {}
        self._is_word = False

    def get_child_at_char(self, c):
        return self._children.get(c, None)

    def add_child_at_char(self, c):
        node = SimpleTrieNode()
        self._children[c] = node
        return node

    def is_word(self):
        return self._is_word

    def set_is_word(self, word):
        self._is_word = word


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
                return False
            curr_node = child

        return curr_node.is_word()

    def find_possible_words(self, letters):
        return frozenset(self._find_possible_words(self._root, letters))

    def _find_possible_words(self, curr_node, remaining, taken=""):
        if not remaining:
            return []

        results = []

        for index in range(0, len(remaining)):
            letter = remaining[index]
            child = curr_node.get_child_at_char(letter)
            if not child:
                continue

            possible_word = taken + letter
            if child.is_word():
                results.append(possible_word)

            results += self._find_possible_words(child, remaining[0:index] + remaining[index + 1:], possible_word)

        return results
