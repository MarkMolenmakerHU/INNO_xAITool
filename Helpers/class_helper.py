from typing import Tuple
from AI_Models.Models.interface_ai_model import InterfaceAiModel
from XAI_Models.Models.interface_xai_model import InterfaceXaiModel
from os.path import split as path_split


def get_file_name(dataset: dict, ai_class: InterfaceAiModel, xai_class: InterfaceXaiModel) -> str:
    """
    Create a file name based on the chosen dataset, ai class and xai class.

    Parameters
    ----------
    dataset
        A dictionary containing the data and all the details about it.
    ai_class
        A refrence to the chosen ai method.
    xai_class
        A refrence to the chosen xai method.

    Returns
    -------
    str
        The combined file name.
    """
    dataset_name, ai_model_name, xai_model_name = get_combination_names(dataset, ai_class, xai_class)
    return f'{dataset_name}_{ai_model_name}_{xai_model_name}.html'


def get_combination_names(dataset: dict, ai_class: InterfaceAiModel, xai_class: InterfaceXaiModel) -> Tuple[str, str, str]:
    """
    Get the file, ai class and xai class name and returns them.

    Parameters
    ----------
    dataset
        A dictionary containing the data and all the details about it.
    ai_class
        A refrence to the chosen ai method.
    xai_class
        A refrence to the chosen xai method.

    Returns
    -------
    tuple
        A tuple of the names of the chosen methods.
    """
    _, dataset_name = path_split(dataset['file_path'])
    ai_model_name = type(ai_class).__name__
    xai_model_name = type(xai_class).__name__
    return dataset_name, ai_model_name, xai_model_name
