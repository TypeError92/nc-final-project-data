def is_anagram(s1: str, s2: str):
    letters1 = sorted(list(s1.replace(' ', '').upper()))
    letters2 = sorted(list(s2.replace(' ', '').upper()))
    return letters1 == letters2