"""
https://rszalski.github.io/magicmethods/
"""

import math

"""
__new__
"""


class inch(float):
    """Convert from meter to inch"""

    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg * 39.37)


meters = 12
print '{0} meters is equal to {1} inches'.format(meters, inch(meters))

"""
__init__ and __del__
"""
from os.path import join


class FileObject:
    """Wrapper for file objects to make sure the file gets closed on deletion."""

    def __init__(self, filepath='~', filename='sample.txt'):
        # open a file filename in filepath in read and write mode
        self.file = open(join(filepath, filename), 'r+')

    def __del__(self):
        self.file.close()
        del self.file


"""
comparison magic methods
"""


class Word(str):
    """Class for words, defining comparison based on word length."""

    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an immutable
        # type, so we have to initialize it early (at creation)
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')]  # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


assert Word('      Hi') < Word('Hello')

import functools


@functools.total_ordering
class NumberA(object):
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


assert NumberA(1) < NumberA(2)
assert NumberA(1) <= NumberA(1)
assert NumberA(1) <= NumberA(2)
assert NumberA(1) == NumberA(1)
assert NumberA(1) >= NumberA(1)
assert NumberA(2) >= NumberA(1)
assert NumberA(2) > NumberA(1)

"""
Unary operators and functions
"""


class NumberB(object):
    def __init__(self, value):
        self.value = value

    def __pos__(self):
        return self.value

    def __neg__(self):
        return -1 * self.value

    def __abs__(self):
        return abs(self.value)


print +NumberB(10)
print -NumberB(10)
print abs(NumberB(-32))
