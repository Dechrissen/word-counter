import re
import codecs
from collections import Counter
#import nltk
#from nltk.corpus import stopwords

#nltk.download('stopwords')
#stop_words = set(stopwords.words('english'))

stop_words = ['your', 'those', 'have', 'herself', 'to', 'from', 'shouldnt', 'as', 'under', 'between', 'did', 'yours', 'wasnt', 'o', 'whom', 'the', "haven't", "you'll", "it's", 'their', 'where', 'is', 'about', 'ourselves', 'doesnt', 'mustnt', "won't", 'she', 'doesn', 'me', 'theirs', "wouldn't", 'couldnt', 'was', 'be', "don't", 'all', 'thatll', 'during', 'own', 'wont', "didn't", 'over', 'his', 'by', 'neednt', 'they', 'few', 'in', 'had', 'before', 'after', 'on', 'you', 'couldn', "shan't", "isn't", "weren't", 'does', 'if', 'no', 've', 'y', 'this', 'or', 'hasnt', 'against', 'up', 'having', 'not', 'such', 'into', "hasn't", 'hers', "doesn't", 'both', 'out', 'so', 'just', 'havent', 'which', 'because', 'her', 'below', 'off', 'youve', 'its', 'are', 'other', 'he', 'shouldve', 'hasn', 'won', 'only', 'arent', 'nor', 'am', 'our', 'above', 'of', 'ma', 'isnt', 'will', 'youre', 'but', 'were', "mightn't", 'werent', 'we', 'why', 'and', 'hadn', 'haven', 'who', 'youll', 'when', 'mustn', "she's", 'him', "shouldn't", 'these', 'himself', 'shan', 'my', "needn't", "that'll", 'what', 'a', 'there', 'mightn', 'any', 'each', 'same', 'shouldn', 'some', 'doing', 'shes', 'myself', "wasn't", 're', 'more', "you're", 'until', 'again', 'too', 'wouldn', 'with', 'm', 'ain', 'wouldnt', 'while', 'being', 'how', 'ours', 'didn', 'then', 'most', 'through', 't', 'should', 'needn', 'do', "couldn't", 'don', "you'd", 'it', 'an', 'weren', "should've", 'than', 'here', 'down', 'aren', 'didnt', 'hadnt', 'has', 'that', 'shant', 'been', 'youd', 'now', 'once', 's', "you've", 'd', 'themselves', 'mightnt', 'them', 'yourself', 'isn', 'll', "aren't", 'dont', 'very', 'for', "hadn't", 'i', 'further', 'at', 'can', "mustn't", 'itself', 'yourselves', 'wasn']

def remove_punctuation(text):
    return re.sub(r'[^\w\s]','', text)

word_frequencies = {}
corpus = ''

filename = 'corpus.txt'
with codecs.open(filename, 'r', encoding='utf8') as file:
    corpus = file.read()

corpus = corpus.split()
corpus = [word.lower() for word in corpus]
filtered_corpus = [word for word in corpus if word not in stop_words]
filtered_corpus = [remove_punctuation(word) for word in filtered_corpus]

counts = dict(Counter(filtered_corpus))

counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

limit = 20
start = 0
for item in counts.keys():
    print(item + ':', counts[item])
    start += 1
    if start >= limit:
        break
