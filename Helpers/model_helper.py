from numpy.random import randint


def train_ai_model(ai_class, dataset):
    print("Training AI-Model...")
    names = {'feature_names': dataset['feature_names'], 'target_names': dataset['target_names']}
    model, data, scores = ai_class.train_model(dataset)
    print("Done training AI-Model!")
    return model, data, names, scores

def train_xai_model(xai_class, model, data, names, file_name):
    print("Training  XAI-Model...")
    i = randint(0, data['X_test'].shape[0])
    features_sample = data['X_test'][i]
    target_sample = model.predict([features_sample])[0]
    result = xai_class.train_model(model, data, names, file_name, features_sample, target_sample)
    print("Done training XAI-Model!")
    return result
