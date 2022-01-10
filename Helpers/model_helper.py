def train_ai_model(ai_class, dataset):
    print("Training AI-Model...")
    names = {'feature_names': dataset.feature_names, 'target_names': dataset.target_names}
    model, data, scores = ai_class.train_model(dataset)
    print("Done training AI-Model!")
    return model, data, names, scores

def train_xai_model(xai_class, model, data, names):
    print("Training  XAI-Model...")
    results = xai_class.train_model(model, data, names)
    print("Done training XAI-Model!")
    return results
