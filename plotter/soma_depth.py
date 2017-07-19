import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

# input1 = 'data/Giorgio-Re/PFC/TDI21301017_cell2_pia_spines.MA1.ASC.swc'
# input_folder = 'data\\Xiaojun-Re\\'
input_folder = 'data\\Xiaojun-Re\\'
# output = 'image/neuron_02.eps'
output = 'image\\soma_depth.csv'

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
    rets = []
    names = []
    for filename in all_files:
        print('processing ' + filename)
        nodes = []
        with open(filename, 'r') as file:
            for line in file:
                if line[0] != '#':
                    nodes.append(Node(line))

        res = 0.0
        tot = 0.0
        for node in nodes:
            if node.type == 1:
                temp = (node.radius) ** 2
                res += temp * (node.Y);
                tot += temp
        res /= tot
        rets.append(res)
        names.append(filename[filename.rfind('\\') + 1:])

    with open(output, 'a') as file:
        for name, res in zip(names, rets):
            file.write(name + ', ' + '{0:.4f}'.format(res) + '\n')
