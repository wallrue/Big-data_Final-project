# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 21:36:00 2022

@author: lemin
"""
import sys
import codecs
from snownlp import normal
from snownlp import seg
import os

if os.path.exists(os.path.join(os.path.abspath(os.getcwd()) , 'bayes_model.py')): #Run from sentiment_model.py
    from bayes_model import Bayes_model
else: #Run from main_model.py
    from sentiment_modeling.bayes_model import Bayes_model



def loadingBar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + ' [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')

class Sentiment_model(object):

    def __init__(self):
        self.classifier = Bayes_model()

    def save(self, fname):
        self.classifier.save(fname)

    def load(self, fname):
        self.classifier.load(fname)

    def handle(self, doc):
        words = seg.seg(doc) #segment the sentences
        words = normal.filter_stop(words)
        return words

    def train(self, neg_docs, pos_docs):
        data = []
        
        bar_idx = 0
        for sent in neg_docs:
            data.append([self.handle(sent), 'neg'])
            bar_idx += 1
            loadingBar(bar_idx,len(neg_docs)+len(pos_docs),2) 
            
        for sent in pos_docs:
            data.append([self.handle(sent), 'pos'])
            bar_idx += 1
            loadingBar(bar_idx,len(neg_docs)+len(pos_docs),2) 
            
        self.classifier.train(data)

    def classify(self, sent):
        ret, prob = self.classifier.classify(self.handle(sent))
        if ret == 'pos':
            return prob
        return 1-prob
    
    def get_vocab(self):
        return self.classifier.get_vocab()


def train(neg_file, pos_file):
    neg = codecs.open(neg_file, 'r', 'utf-8').readlines()
    pos = codecs.open(pos_file, 'r', 'utf-8').readlines()
    neg_docs = []
    pos_docs = []
    
    for line in neg:
        neg_docs.append(line.rstrip("\r\n"))

    for line in pos:
        pos_docs.append(line.rstrip("\r\n"))
        
    global classifier
    classifier = Sentiment_model()
    classifier.train(neg_docs, pos_docs)

def save(fname):
    classifier.save(fname)

def load(fname):
    classifier.load(fname)

def classify(sent):
    return classifier.classify(sent)


# data_snownlp = [os.path.join(os.path.abspath(os.getcwd()) , 'dataset\\neg.txt'), os.path.join(os.path.abspath(os.getcwd()) , 'dataset\\pos.txt')] #Path of dataset
# train(data_snownlp[0],data_snownlp[1]) #Train model
# save(os.path.join(os.path.abspath(os.getcwd()) , 'saved_model\\sentiment_bayes\\sentiment_bayes.marshal')) #Store model 