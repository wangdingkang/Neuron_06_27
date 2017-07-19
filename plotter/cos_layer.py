import numpy as np
import matplotlib.pyplot as plt
import math as mt
import matplotlib.cm as cm
import matplotlib.colors as colors
from mpl_toolkits.mplot3d import Axes3D
import scipy.spatial.distance as ssd


input_file = 'data\\Giorgio-Angle\\layers_angle.csv'
maps = {'L1':1, 'L2':2, 'L3':3, 'L4':4, 'L5a':5, 'L5b':6, 'L6':7}
yts = ['L1', 'L2', 'L3', 'L4', 'L5a', 'L5b', 'L6']

if __name__ == '__main__':
    x, y = [], []
    with open(input_file, 'r') as file:
        file.readline()
        for line in file:
            arr = line.strip().split(',')
            cost = mt.cos(float(arr[1]))
            layer = maps[arr[4]]
            x.append(cost)
            y.append(layer)

    maxy = max(y)
    miny = min(y)
    y = [(i - miny) / ((maxy - miny)) for i in y]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlabel('cos(theta)')
    ax.set_ylabel('layers')
    hist, xedges, yedges = np.histogram2d(x, y, bins=[100, 7])
    # print(hist)
    # colors = hist / np.max(hist)

    xpos, ypos = np.meshgrid(xedges[:-1] , yedges[:-1])
    xpos = xpos.flatten('F')
    ypos = ypos.flatten('F')
    zpos = np.zeros_like(xpos)
    # print(hist)
    norm = hist.sum(axis=0)
    hist = hist / norm.reshape(1, 7)

    dx = 0.02 * np.ones_like(zpos)
    dy = dx.copy()
    dz = hist.flatten()

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='r', alpha=1.0, zsort='max')
    plt.yticks([float(i)/7 for i in range(7)], yts, size='small')
    plt.show()

