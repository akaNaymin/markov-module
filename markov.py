
import numpy as np
import pickle

class Markov(object):

    def __init__(self, text=None):
        self.model = {}
        if text:
            mk = Markov.from_text(text)
            self.model = mk.model

    def insert_line(self, line):
        words = line.split() + ['\n']
        word_count = len(words)
        for idx in range(word_count - 1):
            pair = words[idx:idx+2]
            if pair[0] not in self.model.keys(): # new leader
                self.model[pair[0]] = {pair[1]:1}
            elif pair[1] not in self.model[pair[0]]: # new follwer
                self.model[pair[0]][pair[1]] = 1
            else: # add follower
                self.model[pair[0]][pair[1]] += 1 

    @classmethod
    def from_text(cls, text):
        mk = Markov()
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 0:
                mk.insert_line(line)
        return mk

    @classmethod
    def from_file(cls, path):
        with open(path) as file:
            text = file.read()  
        return cls.from_text(text)

    @classmethod
    def from_pickle(cls, filename):
        mk = Markov()
        mk.model = pickle.load(open(filename, 'rb'))
        return mk

    def to_pickle(self, filename):
        pickle.dump(self.model, open(filename, 'wb'))


    def pick_next(self, word):
        word_chains = self.model
        if word in word_chains:
            options = list(word_chains[word].keys())
            odds = np.array(list(word_chains[word].values())).astype('float')
            odds /= odds.sum()
            odds /= odds.sum()
            return np.random.choice(options, p=odds)


    def gen_chain(self):
        word_chains = self.model
        sentence = np.random.choice(list(word_chains.keys()))
        current = sentence
        while current != '\n':
            current = self.pick_next(current)
            sentence = sentence + ' ' + current
        return sentence


    