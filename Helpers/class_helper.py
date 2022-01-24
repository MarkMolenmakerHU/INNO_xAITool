from os.path import split as path_split


def get_file_name(dataset, ai_class, xai_class):
    dataset_name, ai_model_name, xai_model_name = get_combination_names(dataset, ai_class, xai_class)
    return f'{dataset_name}_{ai_model_name}_{xai_model_name}.html'

def get_combination_names(dataset, ai_class, xai_class):
    _, dataset_name = path_split(dataset['filename'])
    ai_model_name = type(ai_class).__name__
    xai_model_name = type(xai_class).__name__
    return dataset_name, ai_model_name, xai_model_name
