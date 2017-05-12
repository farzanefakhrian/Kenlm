import sys
import nltk

reload(sys)
sys.setdefaultencoding('utf8')

for line in sys.stdin:
    for sentence in nltk.sent_tokenize(line):
        print(' '.join(nltk.word_tokenize(sentence)).lower())
