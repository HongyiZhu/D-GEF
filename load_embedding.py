import numpy as np

def loadEmbedding(file):
    f = open(file, 'r')
    n, d = f.readline().split()
    emb = np.zeros((int(n), int(d)), dtype=np.float)
    for line in f.readlines():
        data = line.split()
        emb[int(data[0])] = data[1:]
    f.close()
    
    return emb