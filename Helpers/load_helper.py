import numpy as np
from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass
from AI_Models.Models.interface_ai_model import InterfaceAiModel


def load_dataset(path):
    file = open(path)
    header = file.readline().strip('\n').split(',')
    rows, cols, target_names = int(header[0]), int(header[1]), np.array([target_name for target_name in header[2:]])
    data = np.loadtxt(file, usecols=range(cols + 1), delimiter=',')
    target = data[:, -1]
    file.close()
    return { 'data': data, 'target': target, 'target_names': target_names, 'feature_names': None, 'filename': path }

def load_ai_model(path):
    ai_class = load_class('ai_module', path, InterfaceAiModel)
    return ai_class

def load_class(module_name, module_path, base_model):
    ai_module = SourceFileLoader(module_name, module_path).load_module()
    inheritance_check = lambda class_type: issubclass(class_type, base_model) and not issubclass(base_model, class_type)
    ai_class = [class_type for name, class_type in getmembers(ai_module, isclass) if inheritance_check(class_type)][0]
    return ai_class()
