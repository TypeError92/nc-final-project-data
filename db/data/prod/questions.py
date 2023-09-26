from parser import rows

questions = list(map(lambda row: {'question': row['question'], 'answer': row['answer']}, rows))
