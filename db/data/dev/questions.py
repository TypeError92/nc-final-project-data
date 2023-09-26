from csv import DictReader
from os import path

folder = path.dirname(path.abspath(__file__))

with open(path.join(folder, 'anagrams.csv'), newline='') as file:
    questions = list(map(lambda row: {'question': row['question'], 'answer': row['answer']}, DictReader(file)))
