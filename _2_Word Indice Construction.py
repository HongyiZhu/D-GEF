# -*- coding: utf-8 -*-

import networkx as nx
import pickle
from case_config import *

length = []
fullwordlist = []
for year in range(2012, 2020):
    for q in range(4):
        filename = "{}{}Q{}.txt".format(case, str(year), str(q + 1))
        f = open(filename, 'rb')
        p = pickle.load(f)
        for r in p:
            id, datetime, wordlist = r[0], r[1], r[2]
            if len(wordlist) < 2:
                continue
            for word in wordlist:
                if word not in fullwordlist:
                    fullwordlist.append(word)
        length.append(len(fullwordlist))
        print("{}{}Q{}\t{}".format(case, str(year), str(q + 1), str(len(fullwordlist))))

g = open("Wordlist-{}.pkl".format(case), 'wb')
pickle.dump(fullwordlist, g)
g.close()
h = open("wordlength-{}.pkl".format(case), "wb")
pickle.dump(length, h)
h.close()
