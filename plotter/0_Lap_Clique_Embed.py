import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import SpectralEmbedding
import os
import numpy as np
from collections import OrderedDict
import matplotlib.patches as mpatches
import pickle

vector_folder = 'vectors//'
cluster_folder = 'cluster//'
image_folder = 'embed//'
clique_file = 'cliques//clique.txt'
dim = 3
N = 53
n_clusters = 4

vec_files = os.listdir(vector_folder)
cluster_files = os.listdir(cluster_folder)

# marker_size = [50 for x in range(N)]
assignments = [0 for x in range(N)]
markers_clique = ['.', '+', 'd', '*', 'x', '^']
legend_clique_texts = ['Others', 'Clique 0', 'Clique 1', 'Clique 2', 'Clique 3', 'Clique 4']
legend_cluster_texts = ['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5']

num_c = 1;
with open(clique_file) as tf:
    for line in tf:
        for s in line.strip().split():
            assignments[int(s) - 1] = num_c
        num_c += 1;



for vfile, cfile in zip(vec_files, cluster_files):

    X = np.loadtxt(os.path.join(vector_folder, vfile))
    model = SpectralEmbedding(n_components=dim, )
    np.set_printoptions(suppress=True)
    Y = model.fit_transform(X)
    cluster_labels = [0 for x in range(N)]

    handles = [None for x in range(len(markers_clique))]

    with open(os.path.join(cluster_folder, cfile)) as tf:
        c_num = 1
        for line in tf:
            s = [int(x) for x in line.strip().split()]
            for si in s:
                cluster_labels[si - 1] = c_num
            c_num += 1
    cluster_labels = np.array(cluster_labels, dtype='float')
    # print(cluster_labels / n_clusters)
    colors = cm.gist_rainbow((cluster_labels - 1)/ n_clusters)
    colors_unique = [cm.gist_rainbow(float(i) / n_clusters) for i in range(n_clusters)]

    # print(colors)
    # print(colors_unique)

    fig = plt.figure(figsize=(9, 6))
    if dim == 3:
        ax = fig.add_subplot(111, projection='3d')
    else:
        ax = fig.add_subplot(111)
    # ax.scatter(Y[:, 0], Y[:, 1], Y[:, 2], marker=markers, s=50, lw=0, alpha=1, c=colors, edgecolor='k')

    if dim == 3:
        for i in range(N):
            # if markers_clique[assignments[i]] != 'x' and markers_clique[assignments[i]] != '+':
            #     ax.scatter(Y[i, 0],Y[i, 1], Y[i, 2], marker=markers_clique[assignments[i]], facecolors='none', s=50, edgecolors=colors[i], linewidths=1)
            # else:
                ax.scatter(Y[i, 0], Y[i, 1], Y[i, 2], marker='.', s=50, c=colors[i])
    else:
        for i in range(N):
            # if markers_clique[assignments[i]] != 'x' and markers_clique[assignments[i]] != '+':
            #     ax.scatter(Y[i, 0],Y[i, 1], marker=markers_clique[assignments[i]], facecolors='none', s=50, edgecolors=colors[i], linewidths=1)
            # else:
            ax.scatter(Y[i, 0], Y[i, 1], marker='.', s=50, c=colors[i])


    ax.grid(False)
    ax.set_title('Laplacian eigenmap embedding (' + cfile[:cfile.find('.')] + ')')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    if dim == 3:
        ax.set_zlabel('z')

    print(num_c)
    # handles = [plt.Line2D([0, 0], [0, 0], color='black', marker=markers_clique[i], markerfacecolor='none', linestyle='') for i in range(num_c)]
    # legend1 = ax.legend(handles, legend_clique_texts[:num_c], loc=2)

    patches = [mpatches.Patch(color=colors_unique[i], label=legend_cluster_texts[i]) for i in range(n_clusters)]
    legend2 = ax.legend(handles=patches, loc=1)
    legend2.draggable(state=True)
    # ax.add_artist(legend1)
    ax.add_artist(legend2)

    # plt.savefig(os.path.join(image_folder, cfile[:cfile.find('.')] + '.eps'), format='eps')


    plt.show()

    # pickle.dump(ax, open(os.path.join(image_folder, cfile[:cfile.find('.')] + '.pickle'), 'wb'))
    # plt.close()