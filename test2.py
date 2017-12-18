# -*- coding: utf-8 -*-
# author:BerryHN
from gensim.models import word2vec
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences=word2vec.Text8Corpus("result.txt")


model = word2vec.Word2Vec(sentences,size=50)


a=model.most_similar(u"精液",topn=5)

for i in a:
    print  i[0]


model.save('model_word2vec_model')




