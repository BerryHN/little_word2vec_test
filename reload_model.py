# -*- coding: utf-8 -*-
# author:BerryHN
import  gensim

new_model = gensim.models.Word2Vec.load('model_word2vec_model')

print(new_model[u'精液'])