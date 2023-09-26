from csv import DictReader

with open('anagrams.csv', newline='') as file:
    questions = list(map(lambda row: {'question': row['question'], 'answer': row['answer']}, DictReader(file)))
