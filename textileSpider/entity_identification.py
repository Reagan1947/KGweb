# -*- coding:utf-8 -*-
from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-10-05', lang='zh', quiet=False)
sentence = '背景大学位于北京'
print(nlp.word_tokenize(sentence))
print(nlp.pos_tag(sentence))
print(nlp.ner(sentence))
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))

