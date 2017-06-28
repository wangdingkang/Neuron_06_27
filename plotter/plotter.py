import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


input = 'data/test.swc'


class Node:

    def __init__(self, str):
        data = str.strip().split()
        self.type = int(data[1])
        self.X = float(data[2])
        self.Y = float(data[3])
        self.Z = float(data[4])
        self.radius = float(data[5])
        self.parent = int(data[6])



if __name__ == '__main__':

    nodes = []

    with open(input, 'r') as file:
        for line in file:
            if line[0] != '#':
                nodes.append(Node(line))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    axons_x, axons_y, axons_z, axons_r = [], [], [], []
    somas_x, somas_y, somas_z, somas_r = [], [], [], []
    dends_x, dends_y, dends_z, dends_r = [], [], [], []

    for node in nodes:
        if node.type == 1:
            somas_x.append(node.X)
            somas_y.append(node.Y)
            somas_z.append(node.Z)
            somas_r.append(node.radius)
        elif node.type == 2:
            axons_x.append(node.X)
            axons_y.append(node.Y)
            axons_z.append(node.Z)
            axons_r.append(node.radius)
        else: # == 3
            dends_x.append(node.X)
            dends_y.append(node.Y)
            dends_z.append(node.Z)
            dends_r.append(node.radius)

    ax.scatter(somas_x, somas_y, somas_z, color='g', s=somas_r)
    ax.scatter(axons_x, axons_y, axons_z, color='r', s=axons_r)
    ax.scatter(dends_x, dends_y, dends_z, color='b', s=dends_r)
    plt.show()