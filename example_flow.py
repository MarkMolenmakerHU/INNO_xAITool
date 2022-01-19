from Helpers import train_ai_model, train_xai_model, get_file_name
from sklearn.datasets import load_iris
from AI_Models.Models import XgbAiModel
from XAI_Models.Models import LimeXaiModel

dataset = load_iris()
ai_class = XgbAiModel()
xai_class = LimeXaiModel()

file_name = get_file_name(dataset, ai_class, xai_class)
model, data, names, scores = train_ai_model(ai_class, dataset)
result = train_xai_model(xai_class, model, data, names, file_name)

print(result)
