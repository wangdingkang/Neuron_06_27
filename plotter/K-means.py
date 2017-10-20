from sklearn.cluster import KMeans
import numpy as np
import os
import matplotlib.pyplot as plt

input_folder = 'vectors//'

files = os.listdir(input_folder)

# print(files)

for file in files:
    print(file)
    my_matrix = np.loadtxt(os.path.join(input_folder, file))
    # print(my_matrix)

    Ks = range(2, 15)
    km = [KMeans(n_clusters=i) for i in Ks]
    score = [km[i].fit(my_matrix).score(my_matrix) for i in range(len(km))]
    plt.plot(Ks, score)
    plt.show()