from __future__ import print_function

# from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.manifold import SpectralEmbedding
from sklearn.manifold import Isomap
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE
import os
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np

input_folder = 'vectors//'
output_folder = 'silhoutte_results//K-means//'
cluster_folder = 'cluster_labels//Kmeans//'

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

if not os.path.exists(cluster_folder):
    os.mkdir(cluster_folder)

files = os.listdir(input_folder)
dim = 3
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
# Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.

silhouetes = []
for file in files:
    X = np.loadtxt(os.path.join(input_folder, file))
    model = SpectralEmbedding(n_components=dim,)
    np.set_printoptions(suppress=True)
    Y = model.fit_transform(X)


    silhouete_temp = []
    for n_clusters in range_n_clusters:
        # Create a subplot with 1 row and 2 columns
        fig = plt.figure()
        ax1 = fig.add_subplot(121)
        ax2 = fig.add_subplot(122, projection='3d')
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, init='k-means++', n_init=100, max_iter=500, random_state=123)
        cluster_labels = clusterer.fit_predict(X)

        cluster_subfolder = str(n_clusters) + '//'
        cluster_tfolder = os.path.join(cluster_folder, cluster_subfolder)
        if not os.path.exists(cluster_tfolder):
            os.mkdir(cluster_tfolder)
        cluster_filename = os.path.join(cluster_tfolder, file[:file.find('_')] + '.txt')

        # cluster_outputs = []
        cluster_labels_copy = cluster_labels.astype(int)
        with open(cluster_filename, 'w') as cluster_output_file:
            for cn in range(n_clusters):
                for i in range(len(cluster_labels_copy)):
                    if cluster_labels_copy[i] == cn:
                        cluster_output_file.write(str(i + 1) + ' ')
                cluster_output_file.write('\n')

        # np.savetxt(cluster_filename, cluster_labels.astype(int), delimiter=' ', fmt='%d')

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print("For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)
        silhouete_temp.append(silhouette_avg)
        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
        ax2.scatter(Y[:, 0], Y[:, 1], Y[:, 2], marker='.', s=50, lw=0, alpha=1,
                    c=colors, edgecolor='k')


        # # Labeling the clusters
        # centers = clusterer.cluster_centers_
        # # Draw white circles at cluster centers
        # ax2.scatter(centers[:, 0], centers[:, 1], marker='o',
        #             c="white", alpha=1, s=200, edgecolor='k')

        # for i, c in enumerate(centers):
        #     ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1,
        #                 s=50, edgecolor='k')
        ax2.grid(False)
        ax2.set_title("Laplacian eigenmap embedding of the data")
        ax2.set_xlabel("x")
        ax2.set_ylabel("y")
        ax2.set_zlabel("z")

        plt.suptitle(("Silhouette analysis for KMeans clustering with descriptor function " + file[:file.find('_')] +
                      " with n_clusters = %d" % n_clusters),
                     fontsize=14, fontweight='bold')
        filename = file[:file.find('_')] + '_' + str(n_clusters) + '.png'

        plt.savefig(os.path.join(output_folder, filename))
        plt.close()

    plt.plot(range_n_clusters, silhouete_temp)
    plt.savefig(os.path.join(output_folder, file[:file.find('_')] + '_silhouette_score.png'))
    plt.close()
    silhouetes.append(silhouete_temp)

silhouetes_numpy = np.array(silhouetes)
ssum = np.sum(silhouetes_numpy, axis=0)
# print(ssum)
plt.plot(range_n_clusters, ssum)
plt.savefig(os.path.join(output_folder, 'total_silhouette_score.png'))
plt.close()