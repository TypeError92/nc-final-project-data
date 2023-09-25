from controllers.utils import is_anagram, is_good_anagram


def test_is_anagram():
    # Returns a boolean
    assert isinstance(is_anagram(('', '')), bool)
    # Returns True for a one-word anagram
    assert is_anagram(('ACT', 'CAT'))
    # Returns False for a one-word non-anagram
    assert not is_anagram(('ACT', 'DOG'))
    # Ignores whitespaces
    assert is_anagram(('THE HOBBIT', 'BOTH BE HIT'))
    # Is case-insensitive
    assert is_anagram(('The Hobbit', 'BOTH BE HIT'))


def test_is_good_anagram():
    # Returns False for non-anagram
    assert not is_good_anagram(('HE HIT BOB', 'THE HOBBIT'))
    # Returns False if there are non-whitelisted common words
    assert not is_good_anagram(('BOB CAN ACT', 'COB BAN ACT'))
    # Returns true if there are no common words
    assert is_good_anagram(('THE HOBBIT', 'BOTH BE HIT'))
    # Allows whitelisted common words
    assert is_good_anagram(('THE HOT BIB', 'THE HOBBIT'))
