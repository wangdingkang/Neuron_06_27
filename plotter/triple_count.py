import numpy as np

input_file1 = 'data\\reduced-distance\\density.txt'
input_file2 = 'data\\reduced-distance\\dvec_0.5_0.5.txt'

if __name__ == '__main__':
    density = []
    dvec = []

    with open(input_file1) as file:
        for line in file:
            temp = line.strip().split()
            density.append(temp)

    with open(input_file2) as file:
        for line in file:
            temp = line.strip().split()
            dvec.append(temp)

    size = len(density)

    density = np.array(density).astype(np.float)
    dvec = np.array(dvec).astype(np.float)

    # print(density)

    cnt = 0
    tot = size * (size - 1) * (size - 2) / 6;

    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                t1 = [density[i][j], density[i][k], density[j][k]]
                t2 = [dvec[i][j], dvec[i][k], dvec[j][k]]
                i1 = t1.index(min(t1))
                i2 = t2.index(min(t2))
                if i1 == i2:
                    cnt += 1

    print(cnt, '/', tot)