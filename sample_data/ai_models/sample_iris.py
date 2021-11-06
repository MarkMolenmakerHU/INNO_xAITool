from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


def train_model(dataset_url):
    names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    dataset = read_csv(dataset_url, names=names)

    # Split-out validation dataset
    array = dataset.values
    x = array[:, 0:4]
    y = array[:, 4]
    x_train, x_validation, y_train, y_validation = train_test_split(x, y, test_size=0.20, random_state=1)

    # Make predictions on validation dataset
    model = SVC(gamma='auto')
    model.fit(x_train, y_train)
    predictions = model.predict(x_validation)

    # Evaluate predictions
    print(accuracy_score(y_validation, predictions))
    print(confusion_matrix(y_validation, predictions))
    print(classification_report(y_validation, predictions))
