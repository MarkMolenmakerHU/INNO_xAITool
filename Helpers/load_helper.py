import numpy as np
from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass


def load_dataset(file_path: str) -> dict:
    """
    Read a file with our headers and creates a dictionary out of it.

    Parameters
    ----------
    file_path
        The path to the file to open.

    Returns
    -------
    dict
        A dictionary containing all the data for a dataset.
    """
    file = open(file_path)
    header = file.readline().strip('\n').split(',')

    feature_columns, target_columns = int(header[0]), int(header[1])
    target_names = np.array([header[target_column] for target_column in range(2, len(header))])

    table = np.loadtxt(file, delimiter=',')
    data = table[:, :feature_columns]
    targets = table[:, feature_columns:(feature_columns + target_columns)]

    file.close()
    return {'data': data, 'targets': targets, 'target_names': target_names, 'feature_names': None, 'file_path': file_path}


def load_class(module_name: str, module_path: str, base_model):
    """
    Load a class based on a file path and a interface.

    Parameters
    ----------
    module_name
        A unique name for the module to load.
    module_path
        The path to the chosen module.
    base_model
        Base class/interface that needs to be on the file.

    Returns
    -------
    loaded_class
        The loaded class of the selected file with the interface.
    """
    module = SourceFileLoader(module_name, module_path).load_module()
    loaded_class = [class_type for name, class_type in getmembers(module, isclass) if inheritance_check(class_type)][0]
    return loaded_class()


def inheritance_check(class_type, base_model):
    return issubclass(class_type, base_model) and not issubclass(base_model, class_type)
