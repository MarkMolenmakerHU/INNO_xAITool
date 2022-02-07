from itertools import product
from Helpers import train_ai_model, train_xai_model, get_file_name
from Datasets.Code import load_iris, load_breast_cancer, load_titanic, load_stock
from AI_Models.Models import DtAiModel, LrAiModel, SvmAiModel, XgbAiModel
from XAI_Models.Models import LimeXaiModel, ShapXaiModel


datasets = [load_iris(), load_breast_cancer(), load_titanic(), load_stock()]
ai_classes = [DtAiModel(), LrAiModel(), SvmAiModel(), XgbAiModel()]
xai_classes = [LimeXaiModel(False), ShapXaiModel(False)]

for dataset, ai_class, xai_class in product(datasets, ai_classes, xai_classes):
    file_name = get_file_name(dataset, ai_class, xai_class)
    model, data, names, scores = train_ai_model(ai_class, dataset)
    result = train_xai_model(xai_class, model, data, names, file_name)
    print(f'{result}\n')
