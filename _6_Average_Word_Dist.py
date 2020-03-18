from itertools import zip_longest
from embedding_comparison import *
from read_wordlist import *
from load_embedding import *
import numpy as np
from case_config import *

def get_average_dist(TS=32):
    total_dist = []
    total_count = []
    for i in range(TS-1):
        ts = i + 1
        prev = loadEmbedding("{}-Embedding".format(case) + str(ts) + ".nv")
        now = loadEmbedding("{}-Embedding".format(case) + str(ts + 1) + ".nv")
        f = open("./{}-anchor{}.pkl".format(case, str(ts)), 'rb')
        ind = pickle.load(f)
        f.close()

        dist = get_embedding_distance(prev, get_rotated_embedding(prev, now, ind))
        count = [1,] * len(dist)

        total_dist = [x + y for x, y in zip_longest(total_dist, dist, fillvalue=0)]
        total_count = [x + y for x, y in zip_longest(total_count, count, fillvalue=0)]

    average_dist = [float(x)/float(y) for x, y in zip(total_dist, total_count)]

    return average_dist

def get_top_n_most_average_dist(n=20):
    dist = get_average_dist(TS=32)
    dist_dict = {i: j for i, j in enumerate(dist)}
    rev_dist_dict = {j: i for i, j in enumerate(dist)}
    k = sorted(rev_dist_dict.keys())[::-1]

    # get top n shifts
    for i in range(n):
        ind = rev_dist_dict[k[i]]
        print(str(ind) + ":\t" + lookup(ind) + "\t\t" + str(k[i]))

def get_top_n_least_average_dist(n=20):
    dist = get_average_dist(TS=32)
    dist_dict = {i: j for i, j in enumerate(dist)}
    rev_dist_dict = {j: i for i, j in enumerate(dist)}
    k = sorted(rev_dist_dict.keys())

    # get top n shifts
    for i in range(n):
        ind = rev_dist_dict[k[i]]
        print(str(ind) + ":\t" + lookup(ind) + "\t\t" + str(k[i]))

get_top_n_most_average_dist(20)

def get_total_average():
    dist = get_average_dist(TS=32)
    dist_dict = {i: j for i, j in enumerate(dist)}
    rev_dist_dict = {j: i for i, j in enumerate(dist)}
    k = sorted(rev_dist_dict.keys())[::-1]

    print(np.mean(dist))


# get_top_average_dist()

# print(get_total_average())