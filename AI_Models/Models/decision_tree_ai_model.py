from AI_Models.Models.interface_ai_model import InterfaceAiModel
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, accuracy_score
from sklearn.tree import DecisionTreeClassifier


class DtAiModel(InterfaceAiModel):
    def train_model(self, dataset):
        # Split-out validation dataset
        X = dataset['data']
        y = dataset['targets']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

        # Make predictions on validation dataset
        model = DecisionTreeClassifier()
        model.fit(X_train, y_train)
        
        # Scoring
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average="macro")

        # Saving results and passing it trough
        data = {'X_train': X_train, 'X_test': X_test, 'y_train': y_train, 'y_test': y_test}
        scores = {'accuracy': accuracy, 'f1': f1}

        return model, data, scores
