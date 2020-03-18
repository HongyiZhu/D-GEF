import igraph
from igraph import *
import re
import math
from case_config import *

yearly_list = [4, 8, 12, 16, 20, 24, 28, 32]

for year in yearly_list:
    print("Descriptive Statistics for Quarter: " + str(year))
    filename = '{}EdgelistOut'.format(case) + str(year) + ".edgelist"
    G = Graph.Read_Ncol(filename, directed=True)
    H = Graph.Read_Ncol(filename, directed=False)
    # print("Number of nodes: " + str(G.vcount()))
    # print("Number of edges: " + str(G.ecount()))
    # print("Diameter is: " + str(G.diameter()))
    # print("Radius is: " + str(G.radius()))
    # print("Density is: " + str(G.density()))
    # print("Average path length is: " + str(G.average_path_length()))
    # print("Clustering coefficient is: " + str(mean(G.transitivity_local_undirected())))
    # print("Average Eccentricity is: " + str(mean(G.eccentricity())))
    # print("Minimum Degree is: " + str(min(G.indegree())))
    # print("Maximum Degree is: " + str(max(G.indegree())))
    # print("Average Degree is: " + str(mean(G.indegree())))
    # print("Minimum Degree is: " + str(min(G.outdegree())))
    # print("Maximum Degree is: " + str(max(G.outdegree())))
    # print("Average Degree is: " + str(mean(G.outdegree())))
    print(str(G.vcount()))
    print(str(G.ecount()))
    print(str(G.diameter()))
    print(str(G.radius()))
    print(str(G.density()))
    print(str(G.average_path_length()))
    print(str(mean(H.transitivity_undirected())))
    print(str(mean(G.eccentricity())))
    print(str(min(G.indegree())))
    print(str(max(G.indegree())))
    print(str(mean(G.indegree())))
    print(str(min(G.outdegree())))
    print(str(max(G.outdegree())))
    print(str(mean(G.outdegree())))
    print ("\n")