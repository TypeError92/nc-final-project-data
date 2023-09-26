from csv import DictReader

with open('anagrams.csv', newline='') as file:
    answers = list(map(lambda row: {'answer': row['answer'], 'category': row['category']}, DictReader(file)))
