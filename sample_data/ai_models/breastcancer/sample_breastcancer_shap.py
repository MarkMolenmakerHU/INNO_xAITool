# import packages
import shap
import xgboost as xgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# import the dataset from Sklearn
from sklearn.datasets import load_breast_cancer

# Read the DataFrame, first using the feature data
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Add a target column, and fill it with the target data
df['target'] = data.target

# Show the first five rows
df.head()

# Set up the data for modelling
y = df['target'].to_frame()
X = df[df.columns.difference(['target'])]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# build model - Xgboost
xgb_mod = xgb.XGBClassifier(random_state=42, gpu_id=0)
xgb_mod = xgb_mod.fit(X_train, y_train.values.ravel())

# make prediction and check model accuracy
y_pred = xgb_mod.predict(X_test)

# Performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

# Generate the Tree explainer and SHAP values
explainer = shap.TreeExplainer(xgb_mod)
shap_values = explainer.shap_values(X)
expected_value = explainer.expected_value

############## visualizations #############
# Generate summary dot plot
shap.summary_plot(shap_values, X, title="SHAP summary plot")

# Generate summary bar plot
shap.summary_plot(shap_values, X, plot_type="bar")

# Generate waterfall plot
shap.plots._waterfall.waterfall_legacy(expected_value, shap_values[79], features=X.loc[79, :], feature_names=X.columns,
                                       max_display=15, show=True)

# Generate dependence plot
shap.dependence_plot("worst concave points", shap_values, X, interaction_index="mean concave points")

# Generate multiple dependence plots
for name in X_train.columns:
    shap.dependence_plot(name, shap_values, X)
shap.dependence_plot("worst concave points", shap_values, X, interaction_index="mean concave points")

# Generate force plot - Multiple rows
shap.force_plot(explainer.expected_value, shap_values[:100, :], X.iloc[:100, :])

# Generate force plot - Single
shap.force_plot(explainer.expected_value, shap_values[0, :], X.iloc[0, :])

# Generate Decision plot
shap.decision_plot(expected_value, shap_values[79], link='logit', features=X.loc[79, :],
                   feature_names=(X.columns.tolist()), show=True, title="Decision Plot")
