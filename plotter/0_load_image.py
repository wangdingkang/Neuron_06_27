import pickle
import matplotlib.pyplot as plt


image_path = 'embed\\euclidean.pickle'


fig_handle = pickle.load(open(image_path,'rb'))
plt.show()