#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markovify
import glob

# use 3 or even 2 to add more nonsense. using 5 will eliminate cross-corpora sentences. so 4 is optimal
STATE_SIZE = 4
SENTENCES = 1000

models = []
for filename in glob.glob("corpus-programming/*.txt"):
    print('Loading file:', filename)
    with open(filename) as f:
        models.append(markovify.Text(f.read(), state_size=STATE_SIZE))

for filename in glob.glob("corpus-veda/*.txt"):
    print('Loading file:', filename)
    with open(filename) as f:
        models.append(markovify.Text(f.read(), state_size=STATE_SIZE))

model = markovify.combine(models)

i = 0
while i < SENTENCES:
    sentence = model.make_sentence()
    if sentence is None:
        continue
    i += 1
    print(sentence)
