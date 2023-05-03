Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Named Entity Extraction
import nltk
from nltk import word_tokenize,pos_tag
sentence = "Python is often used as a support language for software developers, for build control and management, testing, and in many other ways."
tokens = word_tokenize(sentence)
tag=pos_tag(tokens)
tag
[('Python', 'NNP'), ('is', 'VBZ'), ('often', 'RB'), ('used', 'VBN'), ('as', 'IN'), ('a', 'DT'), ('support', 'NN'), ('language', 'NN'), ('for', 'IN'), ('software', 'NN'), ('developers', 'NNS'), (',', ','), ('for', 'IN'), ('build', 'JJ'), ('control', 'NN'), ('and', 'CC'), ('management', 'NN'), (',', ','), ('testing', 'VBG'), (',', ','), ('and', 'CC'), ('in', 'IN'), ('many', 'JJ'), ('other', 'JJ'), ('ways', 'NNS'), ('.', '.')]
ne_tree = nltk.ne_chunk(tag)
ne_tree
Tree('S', [Tree('GPE', [('Python', 'NNP')]), ('is', 'VBZ'), ('often', 'RB'), ('used', 'VBN'), ('as', 'IN'), ('a', 'DT'), ('support', 'NN'), ('language', 'NN'), ('for', 'IN'), ('software', 'NN'), ('developers', 'NNS'), (',', ','), ('for', 'IN'), ('build', 'JJ'), ('control', 'NN'), ('and', 'CC'), ('management', 'NN'), (',', ','), ('testing', 'VBG'), (',', ','), ('and', 'CC'), ('in', 'IN'), ('many', 'JJ'), ('other', 'JJ'), ('ways', 'NNS'), ('.', '.')])
