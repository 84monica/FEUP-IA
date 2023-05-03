import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier

dataset = pd.read_csv('../dataset/Heart Disease - Processed.csv')


# Select features and target variable
features = dataset.columns.tolist()[1:]

X = dataset[features]
y = dataset['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# --------------------- DECISION TREE --------------------- #

# Apply Decision Tree Algorithm
model_dt = DecisionTreeClassifier()
model_dt = model_dt.fit(X_train, y_train)
y_pred = model_dt.predict(X_test)

# Evaluate the model
print("Accuracy: ", model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))

# --------------------- TODO LIST --------------------- #
# - More Evaluation metrics
# - More models