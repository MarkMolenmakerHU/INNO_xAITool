from XAI_Models.Models.interface_xai_model import *
from shap import Explainer, force_plot as shap_force_plot, save_html as shap_save_html


class ShapXaiModel(InterfaceXaiModel):
    def train_model(self, model: Any, data: Dict, names: Dict, file_name: str, chosen_sample: List[float], target_sample: float) -> str:
        explainer = Explainer(model, data['X_train'])
        shap_values = explainer.shap_values(chosen_sample, target_sample)
        plot = shap_force_plot(explainer.expected_value[target_sample], shap_values[target_sample])

        result = f"True value {target_sample} predicted {explainer.expected_value[target_sample]} because"
        shap_save_html(f'Results/{file_name}', plot)
        return result
