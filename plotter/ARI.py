import os
import numpy as np
import networkx as nx
from itertools import *

input_folder = 'cluster\\'

N = 53
K = 8
ERROR = 1e-6
CM2 = N * (N - 1) / 2

metrics = {}

if __name__ == '__main__':

    for root, dirs, files in os.walk(input_folder, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            clusters = []
            with open(filename) as tfile:
                for line in tfile:
                    cluster = [int(x) for x in line.strip().split()]
                    clusters.append(cluster)
            metrics[name] = clusters


    # find cliques in order to find strong groups
    G = np.zeros(N, N)
    for key in metrics:
        clusters = metrics[key]
        for cluster in clusters:
            for item in list(combinations(cluster, 2)):
                G[item[0]][item[1]] += 1
                G[item[1]][item[0]] += 1
    G = G / 8
    print(G)
    Graph = nx.from_numpy_matrix(G)
    cliques = list(nx.find_cliques(Graph))
    print(cliques)

    # calculate ARI & S-index
    methods = list(metrics.keys())
    l = len(methods)
    for m1, m2 in zip(methods, methods):
            cluster_i = metrics[m1]
            cluster_j = metrics[m2]

            P = np.zeros(K, K, dtype=float)
            X = np.zeros(K, K, dtype=float)
            W = np.zeros(K, K, dtype=float)

            sum_rij2, sum_ri2, sum_rj2 = 0, 0, 0

            for i in range(K):
                for j in range(K):
                    ri = cluster_i[i]
                    rj = cluster_j[j]
                    rij = set(ri).intersection(set(rj))
                    W[i][j] = min(len(ri), len(rj))
                    sum_ri2 += len(ri) * (len(ri) - 1) / 2
                    sum_rj2 += len(rj) * (len(rj) - 1) / 2
                    sum_rij2 += len(rij) * (len(rij) - 1) / 2;
                    P[i][j] = float(len(rij)) / len(j)

            sum_ri2 /= K;
            sum_rj2 /= K;
            for i in range(K):
                for j in range(K):
                    X[i][j] = max(P[i][j], P[j][i])
                    if X[i][j] < ERROR:
                        W[i][j] = 0

            sum_W = np.sum(W)
            W = W / sum_W

            print(m1, " ", m2)
            ARI = (sum_rij2 - sum_ri2 * sum_rj2 / CM2) / (0.5 * (sum_ri2 + sum_rj2) - sum_ri2 * sum_rj2 / CM2)
            S = 1 - 4 * sum(np.multiply(np.multiply(W, X), 1 - X))
            print("ARI: ", ARI)
            print("S: ", S)












