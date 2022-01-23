from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass
from os.path import split as path_split 

def get_file_name(dataset, ai_class, xai_class):
    dataset_name, ai_model_name, xai_model_name = get_combination_names(dataset, ai_class, xai_class)
    return f'{dataset_name}_{ai_model_name}_{xai_model_name}.html'

def get_combination_names(dataset, ai_class, xai_class):
    _, dataset_name = path_split(dataset['filename'])
    ai_model_name = type(ai_class).__name__
    xai_model_name = type(xai_class).__name__
    return dataset_name, ai_model_name, xai_model_name

def load_class(module_name, module_path, base_model):
    ai_module = SourceFileLoader(module_name, module_path).load_module()
    inheritance_check = lambda class_type: issubclass(class_type, base_model) and not issubclass(base_model, class_type)
    ai_class = [class_type for name, class_type in getmembers(ai_module, isclass) if inheritance_check(class_type)][0]
    return ai_class()
