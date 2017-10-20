import numpy as np
import os
import scipy.spatial.distance as spd

eps = 1e-6

input_folder = 'data\\L-measures-reduced\\'
input_files = ['AAC_LMeasures-All.csv', 'AAC_LMeasures-Axons.csv', 'AAC_LMeasures-Dendrites.csv']
output_folder = 'image\\'
output_files = ['AAC_DL-All.txt', 'AAC_DL-Axons.txt', 'AAC_DL-Dendrites.txt']

if __name__ == '__main__':

    for input, output in zip(input_files, output_files):
        data = []
        with open(input_folder + input) as temp_file:
            for line in temp_file:
                data.append([float(x) for x in line.strip().split(',')])

        data = np.array(data)
        means = np.mean(data, axis=0)
        stds = np.std(data, axis=0, ddof=1)
        stds[stds < eps] = 1.0

        data = data - means[None, :]
        data = data / stds[None, :]

        np.savetxt(output_folder + output, data, fmt='%.4f', delimiter=' ')

        # pdists = spd.squareform(spd.pdist(data, 'cityblock')).tolist()
        # np.savetxt(output_folder + output, pdists, fmt='%.4f', delimiter=' ')