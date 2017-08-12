import numpy as np
from sklearn.manifold import SpectralEmbedding

dim = 2
t = 0.1
input_axon = 'data\\tSNE\\0.25_0.75.txt'
output_ret = 'output\\0.25_0.75_eig_pers' + str(dim) + '.csv'

if __name__ == '__main__':

    axon = np.loadtxt(input_axon)

    # reduced need to delete the first column
    # axon = axon[:, 1:]

    all = axon; # + dend;

    all = np.exp(- (all ** 2) / t)
    print(all)
    # 'precomputed' means distance matrix, otherwise, it's data points
    model = SpectralEmbedding(n_components=dim, affinity='precomputed')
    np.set_printoptions(suppress=True)
    ret = model.fit_transform(all)

    np.savetxt(output_ret, ret, delimiter=',');