from scipy.cluster import hierarchy
import numpy as np
from scipy.spatial.distance import squareform


input_file = 'cluster//distances.txt'
distances = np.loadtxt(input_file)

linkage = hierarchy.linkage(distances, method='complete')
# print(linkage)


c = hierarchy.fcluster(linkage, 8, criterion='maxclust')
print(c)