from XAI_Models.Models.interface_xai_model import InterfaceXaiModel


class LimeXaiModel(InterfaceXaiModel):
    def train_model(self, dataset_url: str):
        cancer_type = data.target_names[knn.predict(X_test)[0]]
        print(f'True value: {cancer_type}')
        predicter = lambda x: knn.predict_proba(x).astype(float)
        explainer = LimeTabularExplainer(X, feature_names=data.feature_names, class_names=data.target_names, kernel_width=5)
        explanation = explainer.explain_instance(X_test[0], predicter, num_features=10)
        print(explanation.as_list())