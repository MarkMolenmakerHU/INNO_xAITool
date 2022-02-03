import numpy as np
from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass
from AI_Models.Models.interface_ai_model import InterfaceAiModel


def load_dataset(path) -> dict:
    file = open(path)
    header = file.readline().strip('\n').split(',')

    feature_columns, target_columns = int(header[0]), int(header[1])
    target_names = np.array([header[target_column] for target_column in range(2, len(header))])

    table = np.loadtxt(file, delimiter=',')
    data = table[:, :feature_columns]
    targets = table[:, feature_columns:(feature_columns + target_columns)]

    file.close()
    return {'data': data, 'targets': targets, 'target_names': target_names, 'feature_names': None, 'filename': path}

def load_ai_model(path: str):
    ai_class = load_class('ai_module', path, InterfaceAiModel)
    return ai_class

def load_class(module_name: str, module_path: str, base_model):
    ai_module = SourceFileLoader(module_name, module_path).load_module()
    inheritance_check = lambda class_type: issubclass(class_type, base_model) and not issubclass(base_model, class_type)
    ai_class = [class_type for name, class_type in getmembers(ai_module, isclass) if inheritance_check(class_type)][0]
    return ai_class()
