import pickle
from case_config import *

f = open("Wordlist-{}.pkl".format(case), 'rb')
# f = open("Wordlist-GoldStandard.pkl", 'rb')
wordlist = pickle.load(f)


def lookup(i):
    return wordlist[i]


def output():
    f = open("words-{}.csv".format(case), "w", encoding="utf-8")
    for i, w in enumerate(wordlist):
        f.write("{},{}\n".format(str(i), w))
    f.close()

# output()


