from textblob import TextBlob

org = 'programming langage'
print(f'Original text = {org}')

b = TextBlob(org) 
print(f'corrected text = {b.correct()}')