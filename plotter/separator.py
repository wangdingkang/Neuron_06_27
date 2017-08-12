import os

input_folder = 'data\\Xiaojun-Reduced'
output_axon_folder = 'data\\Xiaojun-Axon-Reduced'
output_dend_folder = 'data\\Xiaojun-Dend-Reduced'


if __name__ == '__main__':
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            print(filename)
            temp_axon = []
            temp_dend = []
            fir_axon, fir_dend = -1, -1;
            with open(os.path.join(root, filename)) as temp:
                for line in temp:
                    arr = line.split()
                    if arr[1] == '2':
                        if fir_axon == -1:
                            fir_axon = int(arr[0]) - 1;
                            arr[0] = '1'
                            temp_axon.append(' '.join(arr))
                        else:
                            arr[0] = str(int(arr[0]) - fir_axon)
                            arr[6] = str(int(arr[6]) - fir_axon)
                            temp_axon.append(' '.join(arr))
                    elif arr[1] == '3':
                        if fir_dend == -1:
                            fir_dend = int(arr[0]) - 1;
                            arr[0] = '1'
                            temp_dend.append(' '.join(arr))
                        else:
                            arr[0] = str(int(arr[0]) - fir_dend)
                            arr[6] = str(int(arr[6]) - fir_dend)
                            temp_dend.append(' '.join(arr))

            with open(os.path.join(output_axon_folder, filename), 'a') as faxon:
                for line in temp_axon:
                    faxon.write(line + '\n')

            with open(os.path.join(output_dend_folder, filename), 'a') as faxon:
                for line in temp_dend:
                    faxon.write(line + '\n')
