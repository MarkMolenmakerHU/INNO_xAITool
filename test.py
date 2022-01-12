from Helpers import train_ai_model, train_xai_model
from sklearn.datasets import load_iris, load_breast_cancer
from AI_Models.Models import SvmAiModel, XgbAiModel
from XAI_Models.Models import LimeXaiModel, ShapXaiModel

dataset = load_breast_cancer()
ai_class = XgbAiModel()
xai_class = ShapXaiModel()

model, data, names, scores = train_ai_model(ai_class, dataset)
results = train_xai_model(xai_class, model, data, names)

print(results)
