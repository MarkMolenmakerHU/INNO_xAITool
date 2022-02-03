from numpy import argmax
from XAI_Models.Models.interface_xai_model import *
from shap import KernelExplainer, force_plot as shap_force_plot, save_html as shap_save_html


class ShapXaiModel(InterfaceXaiModel):
    def __init__(self, save_result=True) -> None:
        self.save_result = save_result

    def train_model(self, model: Any, data: Dict, names: Dict, file_name: str, data_sample: List[float], target_sample: float) -> str:
        explainer = KernelExplainer(model.predict_proba, data['X_test'])
        shap_values = explainer.shap_values(data['X_test'])
        predicted = argmax(explainer.expected_value)
        plot = shap_force_plot(predicted, shap_values[0], data_sample, names['feature_names'])
        result = f"True value {target_sample} predicted {explainer.expected_value} because..."
        if self.save_result: shap_save_html(f'Results/{file_name}', plot)
        return result
