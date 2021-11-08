# import packages
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# import the dataset from Sklearn
from sklearn.datasets import load_breast_cancer


def train_model(dataset):
    # Read the DataFrame, first using the feature data
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    # Add a target column, and fill it with the target data
    df['target'] = data.target

    # Show the first five rows
    df.head()

    # Set up the data for modelling
    y = df['target'].to_frame()  # define Y
    X = df[df.columns.difference(['target'])]  # define X
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)  # create train and test

    # build model - Xgboost
    xgb_mod = xgb.XGBClassifier(random_state=42, gpu_id=0)  # build classifier
    xgb_mod = xgb_mod.fit(X_train, y_train.values.ravel())

    # make prediction and check model accuracy
    y_pred = xgb_mod.predict(X_test)

    # Performance
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
