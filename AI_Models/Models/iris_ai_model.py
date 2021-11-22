from AI_Models.Models.interface_ai_model import InterfaceAiModel
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


class IrisAiModel(InterfaceAiModel):
    def train_model(self, dataset_url):
        feature_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        target_names = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        dataset = read_csv(dataset_url, names=feature_names)

        # Split-out validation dataset
        X = dataset.values[:, 0:4]
        y = dataset.values[:, 4]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        # Make predictions on validation dataset
        model = SVC(gamma='auto', probability=True)
        model.fit(X_train, y_train)

        data = {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}
        names = {'feature_names': feature_names, 'target_names': target_names}
        return model, data, names
