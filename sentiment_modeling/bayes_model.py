# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 21:33:55 2022

@author: lemin
"""

import marshal
from math import log, exp
import sys

class AddOneProb(object): 

    def __init__(self):
        self.d = {}
        self.total = 0.0
        self.none = 1
    
    def exists(self, key):
        return key in self.d

    def getsum(self):
        return self.total

    def get(self, key):
        if not self.exists(key):
            return False, self.none
        return True, self.d[key]

    def freq(self, key):
        return float(self.get(key)[1])/self.total

    def samples(self):
        return self.d.keys()
    
    def add(self, key, value):
        self.total += value
        if not self.exists(key):
            self.d[key] = 1
            self.total += 1
        self.d[key] += value
        
class Bayes_model(object):

    def __init__(self):
        self.d = {}
        self.total = 0

    def save(self, fname, iszip=True):
        d = {}
        d['total'] = self.total
        d['d'] = {}
        for k, v in self.d.items():
            d['d'][k] = v.__dict__
            
        if sys.version_info[0] == 3:
            fname = fname + '.3'
        
        marshal.dump(d, open(fname, 'wb'))

    def load(self, fname, iszip=True):
        if sys.version_info[0] == 3:
            fname = fname + '.3'
            d = marshal.load(open(fname, 'rb'))

        self.total = d['total']
        self.d = {}
        for k, v in d['d'].items():
            self.d[k] = AddOneProb()
            self.d[k].__dict__ = v

    def train(self, data):
        for d in data:
            c = d[1]
            if c not in self.d:
                self.d[c] = AddOneProb()
            for word in d[0]:
                self.d[c].add(word, 1)
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))

    def classify(self, x):
        tmp = {}
        for k in self.d:
            tmp[k] = log(self.d[k].getsum()) - log(self.total)
            for word in x:
                tmp[k] += log(self.d[k].freq(word))
        ret, prob = 0, 0
        for k in self.d:
            now = 0
            try:
                for otherk in self.d:
                    now += exp(tmp[otherk]-tmp[k])
                now = 1/now
            except OverflowError:
                now = 0
            if now > prob:
                ret, prob = k, now
        return (ret, prob)
    
    def get_vocab(self):
        dict_ = {'vocab': list(), 'total': 0}
        for k, v in self.d.items():
            dict_['vocab'].extend(list(v.__dict__['d'].keys()))
        dict_['total'] = len(dict_['vocab'])
        return dict_