from sklearn.metrics import f1_score, accuracy_score


def train_model(ai_class, dataset_url):
    print("Training...")
    model, X_test, y_test = ai_class.train_model(dataset_url)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")
    return accuracy, f1
