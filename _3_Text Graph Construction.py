# encoding=utf8

import nltk
import networkx as nx
import pickle
import igraph
from igraph import *
from case_config import *

count = 1
# TODO: Change start/end date/year
for year in range(2012, 2020):
    for q in range(4):
        filename = "{}{}Q{}.txt".format(case, str(year), str(q + 1))
        f = open(filename, 'rb')
        p = pickle.load(f)

        g = open("Wordlist-{}.pkl".format(case), 'rb')
        fullwordlist = pickle.load(g)
        g.close()

        edgelist = []
        edgelistfilename = "{}Edgelist".format(case) + str(count) + ".edgelist"
        edgelistfile = open(edgelistfilename, "w")
        for r in p:
            id, datetime, wordlist = r[0], r[1], r[2]
            if len(wordlist) < 2:
                continue
            for j in range(len(wordlist) - 1):
                # Directed Edges
                edge = str(fullwordlist.index(wordlist[j])) + " " + (str(fullwordlist.index(wordlist[j+1])) + "\n")
                edgelistfile.write(edge)

        edgelistfile.close()
        # G = nx.read_edgelist(edgelistfilename, nodetype=int)
        # print(G.nodes())
        # print(G.edges())

        count += 1