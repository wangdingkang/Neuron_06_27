from sklearn.cluster import KMeans
import numpy as np
import os
import matplotlib.pyplot as plt

input_folder = 'vectors//'
output_folder = 'cluster//'
files = os.listdir(input_folder)

# print(files)
K = 5

for file in files:
    print(file)
    X = np.loadtxt(os.path.join(input_folder, file))


    km = KMeans(n_clusters=5)
    cluster_labels = km.fit_predict(X)
    filename = file[:file.find('_')]

    with open(os.path.join(output_folder, filename + '.txt'), 'w') as tf:
        for k in range(K):
            for i in [x for x in range(len(cluster_labels)) if cluster_labels[x] == k]:
                tf.write(str(i + 1) + ' ')
            tf.write('\n')

    print(cluster_labels)