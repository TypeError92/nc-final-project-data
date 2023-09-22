import pytest
from utils import is_anagram

def test_is_anagram():
    # Returns a boolean
    assert isinstance(is_anagram('', ''), bool)
    # Returns True for a one-word anagram
    assert is_anagram('ACT', 'CAT')
    # Returns False for a one-word non-anagram
    assert not is_anagram('ACT', 'DOG')
    # Ignores whitespaces
    assert is_anagram('THE HOBBIT', 'BOTH BE HIT')
    # Is case-insensitive
    assert is_anagram('The Hobbit', 'BOTH BE HIT')
