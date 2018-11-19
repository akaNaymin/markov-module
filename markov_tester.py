import markov as mc

with open('harry_potter_fanfic.txt') as f:
    text = f.read()

module = mc.markov(text)

print(module.gen_chain())

module.to_pickle('pumparum')