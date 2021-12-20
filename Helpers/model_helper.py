from sklearn.metrics import f1_score, accuracy_score


def train_ai_model(ai_class, dataset_url):
    print("Training AI-Model...")
    model, data, names = ai_class.train_model(dataset_url)
    y_pred = model.predict(data['X_test'])
    accuracy = accuracy_score(data['y_test'], y_pred)
    f1 = f1_score(data['y_test'], y_pred, average="macro")
    scores = { 'accuracy': accuracy, 'f1': f1 }
    return model, data, names, scores

def train_xai_model(xai_class, model, data, names):
    print("Training  XAI-Model...")
    results = xai_class.train_model(model, data, names)
    return results
