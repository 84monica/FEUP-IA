import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from imblearn.over_sampling import SMOTE
from collections import Counter

dataset = pd.read_csv('../dataset/Heart Disease - Processed.csv')

# Select features and target variable
features = dataset.columns.tolist()[1:]

X = dataset[features]
y = dataset['HeartDisease']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# --------------------- SMOTE --------------------- #

smote = SMOTE(random_state = 2)
X_train, y_train = smote.fit_resample(X_train, y_train)

# --------------------- DECISION TREE --------------------- #

time1 = time.time()

# Apply Decision Tree Algorithm
model_dt = DecisionTreeClassifier()
model_dt = model_dt.fit(X_train, y_train)
y_pred = model_dt.predict(X_test)

time2 = time.time()

# Evaluate the model
print("Time spent: ", time2 - time1)
print("Accuracy: ", model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("Confusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- TODO LIST --------------------- #
# TODO: More models