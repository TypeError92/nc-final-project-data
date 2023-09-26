from csv import DictReader

with open('anagrams.csv', newline='') as file:
    rows = list(DictReader(file))
