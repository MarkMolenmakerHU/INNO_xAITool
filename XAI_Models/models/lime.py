from XAI_Models.Models.interface_xai_model import InterfaceXaiModel
from lime.lime_tabular import LimeTabularExplainer
from numpy.random import randint

class LimeXaiModel(InterfaceXaiModel):
    def train_model(self, model, data, names):
        print(f"True value: {model.predict(data['X_test'])[0]}")
        explainer = LimeTabularExplainer(data['X_train'], feature_names=names['feature_names'], class_names=names['target_names'], discretize_continuous=True)
        i = randint(0, data['X_test'].shape[0])
        explanation = explainer.explain_instance(data['X_test'][i], model.predict_proba, num_features=2, top_labels=1)
        results = explanation.as_map()
        return results
