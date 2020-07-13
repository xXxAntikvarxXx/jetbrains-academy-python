dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

not_correct = [word for word in input().split() if word not in dictionary]
print("\n".join(not_correct) if not_correct else "OK")
