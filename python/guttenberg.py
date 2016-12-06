#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Attempt to solve the task from facebook interview."""

import argparse
import logging
from pathlib import Path
import sys

logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class Trie(object):
    """Trie of x option * (char, trie) list."""

    def __init__(self, char):
        """Init Trie with char."""
        self.num = None
        self.char = char
        self.char_of_childs = set()

    def __repr__(self):
        """Pretty print it."""
        return "({}:{} -> {})".format(self.char, self.num,
                                         self.char_of_childs)

    def childs(self):
        """Return children of this Trie."""
        return self.char_of_childs

    def char(self):
        """Return char of this Trie."""
        return self.char

    def _find_child(self, c, childs):
        return filter(lambda ch: ch.char == c, childs)[0]

    def add_normal_char(self, c):
        """Add c to the childs."""
        childs = self.childs()
        chars = map(lambda trie: trie.char, childs)
        if c in chars:
            cur_c = self._find_child(c, childs)
        else:
            new_T = Trie(c)
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

    def add_char(self, c):
        """Add delimter or normal char."""
        if c.isalnum():
            return self.add_normal_char(c.lower())
        else:
            return self.add_delimiter()


def find_char(char, words):
    """Find start-letter between words."""
    c = filter(lambda w: w.char == char, words)
    if c:
        c = c[0]
    return c


def add_str(str, words=set(), log=logging.getLogger()):
    """Add string to the set of words."""
    cur_c = None
    for c in str:
        if cur_c:  # add letter to the current word
            cur_c = cur_c.add_char(c)
        else:  # begin new word
            cur_c = find_char(c, words)
            if not cur_c:
                cur_c = Trie(c)
                words = words | set([cur_c])
    else:
        if cur_c:
            cur_c.add_delimiter()
    return words


def handle_file(fn, words=set([])):
    """Extract words from file fn."""
    f = open(fn, 'r')
    for line in f:
        words = add_str(line, words)
    return words

def words2list(words, lst=[]):
    for word in words:




def main(fn, num):
    """Main entry point."""
    words = set([])
    p = Path(fn)
    if p.is_file() and p.exists():
        words = handle_file(p.as_posix(), words)
    else:
        for f in p.iterdir():
            if f.exists():
                words = handle_file(f.as_posix(), words)
    print words
    sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help=("file/path to dir with files"
                                      "with text for calculation"))
    parser.add_argument("-n", "--num", help="amount of most frequent words",
                        default=10, type=int)
    args = parser.parse_args()
    main(args.path, args.num)
