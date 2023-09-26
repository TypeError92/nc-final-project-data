from parser import rows

answers = list(map(lambda row: {'answer': row['answer'], 'category': row['category']}, rows))
