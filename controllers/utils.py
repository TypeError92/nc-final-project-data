def is_anagram(pair: tuple[str, str]):
    s1, s2 = pair
    letters1 = sorted(list(s1.replace(' ', '').upper()))
    letters2 = sorted(list(s2.replace(' ', '').upper()))
    return letters1 == letters2
