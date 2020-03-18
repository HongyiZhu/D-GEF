from embedding_comparison import *
from read_wordlist import *
from rload_embedding import *
import numpy as np
from case_config import *

# TODO: change the scope of comparison
ts1 = 1
ts2 = 32

e1 = loadEmbedding("{}-Embedding{}.nv".format(case, str(ts1)))
e2 = loadEmbedding("{}-Embedding{}.nv".format(case, str(ts2)))
f = open("./{}-anchor{}.pkl".format(case, str(ts1)), 'rb')
ind = pickle.load(f)
f.close()


def get_top_shifts(prev, now):
    dist = get_embedding_distance(prev, get_rotated_embedding(prev, now, ind))
    dist_dict = {i: j for i, j in enumerate(dist)}
    rev_dist_dict = {j: i for i, j in enumerate(dist)}
    k = sorted(rev_dist_dict.keys())[::-1]

    # get top n shifts
    n = 20
    for i in range(n):
        ind = rev_dist_dict[k[i]]
        print(str(ind) + ":\t" + lookup(ind) + "\t\t" + str(k[i]))

def get_top_sim_diff(prev, now):
    pairlist, sim_diff = get_embedding_cosine_diff(prev, get_rotated_embedding(prev, now, ind))
    sim_diff_dict = {pairlist[i]: sim_diff[i] for i in range(len(pairlist))}
    rev_sim_diff_dict = {sim_diff[i]: pairlist[i] for i in range(len(pairlist))}
    l = sorted(rev_sim_diff_dict.keys())  # decrease in sim
    k = sorted(rev_sim_diff_dict.keys())[::-1] # increase in sim

    # Max n1 sim increase
    n1 = 20
    for i in range(n1):
        ind = rev_sim_diff_dict[k[i]]
        print("(" + lookup(ind[0]) + "," + lookup(ind[1]) + "):\t\t" + str(k[i]))

    # Max n2 sim decrease
    n2 = 20
    for i in range(n2):
        ind = rev_sim_diff_dict[l[i]]
        print("(" + lookup(ind[0]) + "," + lookup(ind[1]) + "):\t\t" + str(l[i]))

get_top_shifts(e1, e2)
# print("====")
# get_top_sim_diff(e1, e2)
# print("====")
# get_top_sim_diff(center(e1), center(e2))