
import numpy as np
import pickle

class markov():

    def __init__(self, text):
        self.model = {}
        self.create_markov(text)

    def parse_line(self, line):
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

    def create_markov(self, text):
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 0:
                self.parse_line(line)

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

    def to_pickle(self, filename):
        pickle.dump(self.model, open('pickled_markov.p', 'wb'))

    def from_pickle(self, filename):
        self.model = pickle.load(open('pickled_markov.p', 'rb'))