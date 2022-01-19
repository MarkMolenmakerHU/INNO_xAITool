from XAI_Models.Models.interface_xai_model import *
from lime.lime_tabular import LimeTabularExplainer


class LimeXaiModel(InterfaceXaiModel):
    def train_model(self, model: Any, data: Dict, names: Dict, file_name: str, chosen_sample: List[float], target_sample: float) -> str:
        explainer = LimeTabularExplainer(data['X_train'], feature_names=names['feature_names'], class_names=names['target_names'], discretize_continuous=True)
        explanation = explainer.explain_instance(chosen_sample, model.predict_proba, num_features=2, top_labels=1)
        exp_map = explanation.as_map()

        predicted = list(exp_map)[0]
        reason = ' and '.join([f'feature {feature} has a weight of {weight}' for feature, weight in exp_map[predicted]])
    
        result = f"True value {target_sample} predicted {predicted} because {reason}"
        explanation.save_to_file(f'Results/{file_name}')
        return result
