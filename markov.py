
import numpy as np


class markov():

    def __init__(self, text):
        self.model = self.make_markov(text)

    def make_markov(self, text):
        word_chains = {}
        for line in text.split('\n'):
            line = line.strip()
            if len(line) > 0:
                words = line.split() + ['\n']
                word_count = len(words)
                for idx in range(word_count - 1):
                    pair = words[idx:idx+2]
                    if pair[0] not in word_chains.keys():
                        word_chains[pair[0]] = {pair[1]:1}
                    elif pair[1] not in word_chains[pair[0]]:
                        word_chains[pair[0]][pair[1]] = 1
                    else:
                        word_chains[pair[0]][pair[1]] += 1
        return word_chains


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


