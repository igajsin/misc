#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Attempt to solve the task from facebook interview."""

cur_c = None

words = set()

class Trie(object):
    """Trie of x option * (char, trie) list."""

    def __init__(self, char, parent=None):
        """Init Trie with char."""
        self.num = None
        self.char = char
        self.char_of_childs = set()
        self.parent = parent

    def __repr__(self):
        """Pretty print it."""
        parent = ""
        if self.parent:
            parent = "{}:{}".format(self.parent.char, self.parent.num)

        return "({}|{}:{} -> {})".format(parent, self.char, self.num,
                                         self.char_of_childs)

    def childs(self):
        """Return children of this Trie."""
        return self.char_of_childs

    def char(self):
        """Return char of this Trie."""
        return self.char

    def _find_child(self, c, childs):
        return filter(lambda ch: ch.char == c, childs)[0]

    def add_to_parent(self, n):
        """Add n to the parent.num."""
        parent = self.parent
        if parent.num:
            parent.num += 1
        else:
            parent.num = 1

    def add_normal_char(self, c):
        """Add c to the childs."""
        childs = self.childs()
        chars = map(lambda trie: trie.char, childs)
        if c in chars:
            cur_c = self._find_child(c, childs)
        else:
            new_T = Trie(c, self)
            self.char_of_childs = self.char_of_childs | set([new_T])
            cur_c = new_T
        return cur_c

    def add_delimiter(self):
        """If we have a delimter, the word is done. Inc counter."""
        if self.num:
            self.num += 1
        else:
            self.num = 1
        return None


def main():
    """Main entry point."""
    pass


if __name__ == "__main__":
    main()

def add_word(str, trie):
    cur_c = trie
    for c in str:
	cur_c = cur_c.add_normal_char(c)
    cur_c.add_delimiter()
    return trie
