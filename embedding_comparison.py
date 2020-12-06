from numpy.linalg import svd
import numpy as np


# Recommend centering the embedding prior to applying the distance/similarity calculations.


def get_rotation_matrix(E_prev, E_now): 
    """
    This method is used to get the rotation matrix. The problem formulation and solution can be found on:
    https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem

    R = argmin(Q) ||QE_new - E_prev||
    Solution: 
    M = E_prev x E_new^T
    U, S, V^T = SVD(M)
    R = U x V^T
    
    :param E_prev: The embedding of the previous TimeSpell, size of n x d, where n is the number of nodes, d is the dimension of the embedding space.
    :param E_now: The embedding of the current TimeSpell, size of n x d, where n is the number of nodes, d is the dimension of the embedding space.
    :return: Returns the rotation matrix of the embedding space.
    """
    T_prev = E_prev.T
    T_now = E_now.T
    M = np.dot(T_prev, T_now.T)
    U, S, Vh = svd(M)
    # print(U.shape, S.shape, Vh.shape)
    R = np.dot(U, Vh)

    return R


def get_rotated_embedding(E_prev, E_now, ind):
    """
    This method returns the rotated embedding of E_now.
    """
    # Use the anchor nodes to compute the rotation matrix for the embedding space.
    E_prev_anchor = np.zeros((len(ind), E_prev.shape[1]), dtype=np.float)
    for i, idx in enumerate(ind):
        E_prev_anchor[i] = E_prev[int(idx)]
    E_now_anchor = np.zeros((len(ind), E_prev.shape[1]), dtype=np.float)
    for i, idx in enumerate(ind):
        E_now_anchor[i] = E_now[int(idx)]
    
    R = get_rotation_matrix(E_prev_anchor, E_now_anchor)
    # Transpose E_now first to align the dimensions, apply the rotation to it, and transpose the result back.
    E_now_rotated = np.dot(R, E_now.T).T

    return E_now_rotated


def get_embedding_distance(E_prev, E_now_rotated):
    n = E_prev.shape[0]
    E_now_rotated_first_n = E_now_rotated[:n, :]
    temp = np.square(np.subtract(E_prev, E_now_rotated_first_n))
    # Measuring the Euclidean distance for each node existed in E_prev
    dist = np.sqrt(np.sum(temp, axis=1))

    return dist


def get_embedding_cosine(E_prev, E_now_rotated):
    n = E_prev.shape[0]
    E_now_rotated_first_n = E_now_rotated[:n, :]
    mode_prev = np.sqrt(np.sum(np.square(E_prev), axis=1))
    mode_now = np.sqrt(np.sum(np.square(E_now_rotated_first_n), axis=1))
    product = np.sum(np.multiply(E_prev, E_now_rotated_first_n), axis=1)
    # Measuring the Cosine Similarity for each node existed in E_prev
    sim = np.divide(np.divide(product, mode_prev), mode_now)

    return sim
