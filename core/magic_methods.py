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
class Number:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value


assert Number(1) < Number(2)
assert Number(1) <= Number(1)
assert Number(1) <= Number(2)
assert Number(1) == Number(1)
assert Number(1) >= Number(1)
assert Number(2) >= Number(1)
assert Number(2) > Number(1)



