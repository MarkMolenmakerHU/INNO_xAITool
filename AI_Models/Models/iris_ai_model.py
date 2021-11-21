from AI_Models.Models.interface_ai_model import InterfaceAiModel
from numpy.lib.function_base import average
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


class IrisAiModel(InterfaceAiModel):
    def train_model(self, dataset_url):
        names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
        dataset = read_csv(dataset_url, names=names)

        # Split-out validation dataset
        X = dataset.values[:, 0:4]
        y = dataset.values[:, 4]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        # Make predictions on validation dataset
        model = SVC(gamma='auto')
        model.fit(X_train, y_train)

        return model, X_test, y_test
