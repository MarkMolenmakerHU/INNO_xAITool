import numpy as np


def load_file(path):
    file = open(path)
    header = file.readline().strip('\n').split(',')
    rows, cols, target_names = int(header[0]), int(header[1]), np.array([target_name for target_name in header[2:]])
    data = np.loadtxt(file, usecols=range(cols + 1), delimiter=',')
    target = data[:, -1]
    file.close()
    return { 'data': data, 'target': target, 'target_names': target_names, 'feature_names': None, 'filename': path }
