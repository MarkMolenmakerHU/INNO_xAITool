from importlib.machinery import SourceFileLoader
from inspect import getmembers, isclass


def load_class(module_name, module_path, base_model):
    ai_module = SourceFileLoader(module_name, module_path).load_module()
    inheritance_check = lambda class_type: issubclass(class_type, base_model) and not issubclass(base_model, class_type)
    ai_class = [class_type for name, class_type in getmembers(ai_module, isclass) if inheritance_check(class_type)][0]
    return ai_class()
