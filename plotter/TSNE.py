import numpy as np
from sklearn.manifold import TSNE

dim = 3
input_axon = 'data\\tSNE\\0.5_0.5.txt'
output_ret = 'output\\0.5_0.5_tsne_pers' + str(dim) + '.csv'

if __name__ == '__main__':

    axon = np.loadtxt(input_axon)

    # reduced need to delete the first column
    # axon = axon[:, 1:]

    all = axon; # + dend;

    # 'precomputed' means distance matrix, otherwise, it's data points
    model = TSNE(n_components=dim, n_iter=5000, random_state=0, metric='precomputed')
    np.set_printoptions(suppress=True)
    ret = model.fit_transform(all)

    np.savetxt(output_ret, ret, delimiter=',');