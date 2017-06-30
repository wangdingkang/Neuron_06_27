import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# input1 = 'data/Giorgio-Re/PFC/TDI21301017_cell2_pia_spines.MA1.ASC.swc'
input_folder = 'data\\Xiaojun-Re\\'
# output = 'image/neuron_02.eps'
output_folder = 'image\\'

class Node:

    def __init__(self, str):
        data = str.strip().split()
        self.type = int(data[1])
        self.X = float(data[2])
        self.Y = float(data[3])
        self.Z = float(data[4])
        self.radius = float(data[5])
        self.parent = int(data[6])


def fetch_files(all_files):
    for root, dirs, files in os.walk(input_folder, topdown=False):
        for name in files:
            all_files.append(os.path.join(root, name))


if __name__ == '__main__':

    all_files = []
    fetch_files(all_files)
    for filename in all_files:
        print('processing ' + filename)
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.view_init(azim=-90, elev=90)
        nodes = []
        with open(filename, 'r') as file:
            for line in file:
                if line[0] != '#':
                    nodes.append(Node(line))

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
        ax.scatter(axons_x, axons_y, axons_z, color='b', s=axons_r)
        ax.scatter(dends_x, dends_y, dends_z, color='r', s=dends_r)

        fig.savefig(output_folder + filename[filename.rfind('\\') + 1:filename.rfind('.')] + '.eps', format='eps', dpi=1000)
        plt.close(fig)