from Bio import Phylo
from io import StringIO
from Bio.Phylo.Consensus import *

input_file_dens = 'data\\consensus-tree\\links_density.txt'
input_file_pers = 'data\\consensus-tree\\links_pers.txt'

SIZE = 53

if __name__ == '__main__':

    density = [str(i) for i in range(1, 54)]
    pers = [str(i) for i in range(1, 54)]

    with open(input_file_dens) as file:
        for line in file:
            data = line.strip().split()
            s = '(' + density[int(data[0]) - 1] + ', ' + density[int(data[1]) - 1] + ')'
            density.append(s)

    print(density[-1])

    with open(input_file_pers) as file:
        for line in file:
            data = line.strip().split()
            s = '(' + pers[int(data[0]) - 1] + ', ' + pers[int(data[1]) - 1] + ')'
            pers.append(s)

    print(pers[-1])

    tree_density = Phylo.read(StringIO(density[-1]), "newick")
    tree_pers = Phylo.read(StringIO(pers[-1]), 'newick')
    trees = [tree_density, tree_pers]
    strict_tree = strict_consensus(trees)
    # majority_tree = majority_consensus(trees, 0.5)
    adam_tree = adam_consensus(trees)
    Phylo.draw(adam_tree)
