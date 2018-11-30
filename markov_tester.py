import markov as mc

with open('harry_potter_fanfic.txt') as f:
    text = f.read()

module1 = mc.Markov(text)
# module2 = mc.Markov.from_file('harry_potter_fanfic.txt')
# module4 = mc.Markov.from_pickle('pickled_markov.p')



# print(module2.gen_chain())
# print(module4.gen_chain())
print(module1.gen_chain())


# module1.to_pickle('pumparum.p')