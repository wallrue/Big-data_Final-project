# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 02:25:48 2022

@author: lemin
"""

import pandas as pd
import os
import gensim
from snownlp import SnowNLP
from snownlp import normal
from snownlp import seg

import gensim.corpora as corpora
from tqdm import tqdm

from .sentiment_model import Sentiment_model


class Sentiment_classfifier(object):
    
    def __init__(self, modelpath):
        self.classifier = Sentiment_model()
        self.classifier.load(modelpath)
        
        self.vocab_dict = self.classifier.get_vocab()['vocab']
        
    def save(self, file_path):
        self.lda_model.save(file_path)
        
    def load(self, file_path):
        self.lda_model = gensim.models.ldamodel.LdaModel.load(file_path, mmap='r')
        
    def handle(self, doc):
        han_text = normal.zh2hans(doc) #Conver Traditional chinese to simplfied chinese
        words = seg.seg(han_text) #segment the sentences
        #words = normal.filter_stop(words)
        filtered_list = [value for value in words if value in self.vocab_dict]
        
        return filtered_list
    
    def sent_to_words(self, sentences): #Preprocess data
        word_list = list()
        for i in tqdm(range(len(sentences))):
            word_list.append(self.handle(sentences[i]))
        return word_list
    
    def sentiment_score(self,key_words): #Mark data   
        corpus_dict = dict()
        for key_word in key_words:
            if key_word in corpus_dict:
                corpus_dict[key_word] = corpus_dict[key_word] + self.classifier.classify(key_word)
            else:
                corpus_dict[key_word] = self.classifier.classify(key_word)
        return corpus_dict
    
    def pre_process(self, contents):
        data_words = self.sent_to_words(contents)
        
        corpus = list()
        for i in tqdm(range(len(data_words))):
            corpus.append(self.sentiment_score(data_words[i]))
            
        id2word = corpora.Dictionary(data_words)

        corpus_list = list()
        for i in tqdm(range(len(corpus))):
            sentence_list = list()
            for key in corpus[i]:
                sentence_list.append((*id2word.doc2idx([key]) , corpus[i][key])) #append((token, score))
            corpus_list.append(sentence_list)
        
        return corpus_list, id2word
    
    
    def predict(self, contents):

        corpus_list, id2word = self.pre_process(contents)   
        sentences = list();
        for predict in corpus_list:
            temp_list = [i[1] for i in predict]
            sentences.append(0 if sum(temp_list)/len(temp_list) < 0.5 else 1)

        return sentences