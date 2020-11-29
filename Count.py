import re
import codecs
import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('stopwords')

def remove_punctuation(text):
    return re.sub(r'[^\w\s]','', text).lower()

word_frequencies = {}
corpus = ''

filename = 'corpus.txt'
with codecs.open(filename, 'r', encoding='utf8') as file:
    corpus = file.read()

stop_words = set(stopwords.words('english'))

corpus = remove_punctuation(corpus)
corpus = corpus.split()
filtered_corpus = [word for word in corpus if word not in stop_words]

counts = dict(Counter(filtered_corpus))

counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

limit = 20
start = 0
for item in counts.keys():
    print(item + ':', counts[item])
    start += 1
    if start >= limit:
        break
