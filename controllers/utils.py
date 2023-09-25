def is_anagram(pair: tuple[str, str]):
    s1, s2 = pair
    letters1 = sorted(list(s1.replace(' ', '').upper()))
    letters2 = sorted(list(s2.replace(' ', '').upper()))
    return letters1 == letters2


def is_good_anagram(pair: tuple[str, str]):
    if not is_anagram(pair):
        return False
    s1, s2 = pair
    common_words = set(s1.split(' ')) & set(s2.split(' '))
    for common_word in common_words:
        if common_word not in ['A', 'I', 'THE']:
            return False
    return True
