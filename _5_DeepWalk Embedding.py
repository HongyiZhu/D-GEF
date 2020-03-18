from openne.node2vec            import Node2vec
from openne.graph               import Graph
import networkx as nx
import operator
import pickle
from case_config import *

embedding_size = 128
window_size = 10                # for DeepWalk and Node2vec
walk_length = 80                # for DeepWalk and Node2vec
number_walks = 10               # for DeepWalk and Node2vec
workers = 8                     # for DeepWalk and Node2vec

# TODO: Change the number of TS
for TS in range(32):
    edgelist_filename = "{}EdgelistOut".format(case) + str(TS+1) + ".edgelist"
    g = Graph()
    print("Reading Edgelist...")
    g.read_edgelist(filename=edgelist_filename, weighted=False, directed=True)

    # DeepWalk OpenNE
    print("DeepWalk processing...")
    model_deepwalk = Node2vec(graph=g, path_length=walk_length, num_paths=number_walks, 
                    dim=embedding_size, window=window_size, workers=workers, dw=True)
    model_deepwalk.save_embeddings("{}-Embedding{}.nv".format(case, str(TS+1)))
    print("DeepWalk finished")

    G = nx.read_edgelist("{}EdgelistOut".format(case) + str(TS+1) + ".edgelist", create_using=nx.DiGraph())
    degrees = G.degree()
    list_degrees = list(degrees)
    list_degrees.sort(key = operator.itemgetter(1), reverse=True)
    
    f = open("./{}-anchor{}.pkl".format(case, str(TS+1)), "wb")
    index = [i for (i,d) in list_degrees[:embedding_size]]
    pickle.dump(index, f)
    f.close()
