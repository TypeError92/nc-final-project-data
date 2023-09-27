from csv import DictReader
from os import path

folder = path.dirname(path.abspath(__file__))

with open(path.join(folder, 'anagrams.csv'), newline='') as file:
    answers = list(map(lambda row: {
        'answer': row['answer'],
        'category': row['category'],
        'subcategory': row['subcategory']
    }, DictReader(file)))
