from XAI_Models.Models.interface_xai_model import InterfaceXaiModel
from numpy.random import randint
from shap import Explainer, force_plot as shap_force_plot


class ShapXaiModel(InterfaceXaiModel):
    def train_model(self, model, data, names):
        i = randint(0, data['X_test'].shape[0])
        expected_value = model.predict(data['X_test'])[0]
        print(f"True value: {expected_value}")
        
        explainer = Explainer(model, data['X_train'])
        shap_values = explainer.shap_values(data['X_test'])
        shap_force_plot(explainer.expected_value, explainer.expected_value, data['X_test'])
        return None
