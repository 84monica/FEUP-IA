import time
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

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

model_dt = DecisionTreeClassifier()
model_dt = model_dt.fit(X_train, y_train)
y_pred = model_dt.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nDecision Tree ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix\n\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- NEURAL NETWORK --------------------- #

time1 = time.time()

model_nn = MLPClassifier(hidden_layer_sizes=10)
model_nn.fit(X_train, y_train)
y_pred = model_nn.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nNeural Network ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_nn.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- NAIVE BAYES --------------------- #

time1 = time.time()

model_nb = GaussianNB()
model_nb.fit(X_train, y_train)
y_pred = model_nb.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nNaive Bayes ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_nb.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- RANDOM FOREST --------------------- #

time1 = time.time()

model_rf = RandomForestClassifier()
model_rf.fit(X_train, y_train)
y_pred = model_rf.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nRandom Forest ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_rf.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- SVM --------------------- #

time1 = time.time()

model_svm = SVC()
model_svm.fit(X_train, y_train)
y_pred = model_svm.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nSVM ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_svm.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- LINEAR REGRESSION --------------------- #

time1 = time.time()

model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
y_pred = model_lr.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nLinear Regression ---------------------\n")
print("Time spent: ", time2 - time1)
print("Mean Squared Error: ", metrics.mean_squared_error(y_test, y_pred))
print("R-squared: ", metrics.r2_score(y_test, y_pred))

# --------------------- LOGISTIC REGRESSION --------------------- #

time1 = time.time()

model_lr = LogisticRegression()
model_lr.fit(X_train, y_train)
y_pred = model_lr.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nLogistic Regression ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_lr.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))

# --------------------- K-NN --------------------- #

time1 = time.time()

model_knn = KNeighborsClassifier()
model_knn.fit(X_train, y_train)
y_pred = model_knn.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nK-NN ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_knn.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))
