import numpy as np
import matplotlib.pyplot as plt
import math as mt
import matplotlib.cm as cm
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
import scipy.spatial.distance as ssd


input_file = 'data\\Giorgio-Angle\\layers_angle.csv'
output_file = 'image\\ret.csv'
NORMALIZE = True


if __name__ == '__main__':
    x, y = [], []
    with open(input_file, 'r') as file:
        file.readline()
        for line in file:
            arr = line.strip().split(',')
            theta = mt.cos(float(arr[1]))
            depth = float(arr[3])
            x.append(theta)
            y.append(depth)

    maxy = max(y)
    miny = min(y)
    y = [(i - miny) / ((maxy - miny)) for i in y]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('cos(theta)')
    ax.set_ylabel('depth')
    hist, xedges, yedges = np.histogram2d(x, y, bins=[100, 10])
    np.savetxt('image\\yedges.csv', yedges, delimiter='\t\n', fmt='%.4f')
    np.savetxt('image\\xedges.csv', xedges, delimiter=' ', fmt='%.4f')
    # print(hist)
    # colors = hist / np.max(hist)

    xpos, ypos = np.meshgrid(xedges[:-1] , yedges[:-2])
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)
    # print(hist)
    norm = hist.sum(axis=0)
    np.savetxt('image\\norm.csv', norm, delimiter='\t\n', fmt='%.4f')


    hist = hist / norm.reshape(1, 10)
    hist = np.delete(hist, 9, 1)

    np.savetxt('image\\normalized_hist.csv', hist, delimiter=' ', fmt='%.4f')

    dx = 0.02 * np.ones_like(zpos)
    dy = dx.copy()
    dz = hist.flatten()

    # offset = dz + np.abs(dz.min())
    # fracs = offset.astype(float) / offset.max()
    # norm = colors.Normalize(fracs.min(), fracs.max())
    # colors = cm.jet(norm(fracs))

    # cm = plt.cm.get_cmap('RdYlBu_r')
    #
    # for x in np.nditer(colors, op_flags=['readwrite']):
    #     x = cm(x)
    #     print(x)

    p = ssd.squareform(ssd.pdist(hist.T, metric='euclidean'))
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r', alpha=1.0, zsort='max')
    plt.show()

    # np.savetxt(output_file, p, delimiter=',', fmt='%.4f')
    #
    # plt.imshow(hist.T, cmap='jet', interpolation='nearest')
    # plt.colorbar()
    # plt.show()