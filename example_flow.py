from Helpers import train_ai_model, train_xai_model, get_file_name
from Datasets.Code import load_iris, load_breast_cancer, load_titanic, load_stock
from AI_Models.Models import DtAiModel, LrAiModel, SvmAiModel, XgbAiModel
from XAI_Models.Models import LimeXaiModel, ShapXaiModel


dataset = load_iris()
ai_class = DtAiModel()
xai_class = LimeXaiModel()

file_name = get_file_name(dataset, ai_class, xai_class)
model, data, names, scores = train_ai_model(ai_class, dataset)
result = train_xai_model(xai_class, model, data, names, file_name)

print(scores)
print(result)
