import time
import pandas as pd
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, GridSearchCV, cross_val_score
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
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../dataset/Heart_Disease_Processed.csv')

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
model_dt.fit(X_train, y_train)
model_dt.score(X_test, y_test)

y_pred = model_dt.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nDecision Tree ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))
print("\nClassification report:\n\n", classification_report(y_test, y_pred))

# --------------------- DECISION TREE CROSS VALIDATION --------------------- #

# K-Fold Cross Validation

model_dt = DecisionTreeClassifier(random_state=42)
k_folds = KFold(n_splits = 5)
scores = cross_val_score(model_dt, X, y, cv = k_folds)

print("\nDecision Tree using K-fold Cross Validation ---------------------\n")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores)) 
print("\n\n")

# Stratified K-Fold

model_dt = DecisionTreeClassifier(random_state=42)
sk_folds = StratifiedKFold(n_splits = 5)
scores = cross_val_score(model_dt, X, y, cv = sk_folds)

print("\nDecision Tree using Stratified K-fold Cross Validation ---------------------\n")
print("Cross Validation Scores: ", scores)
print("Average CV Score: ", scores.mean())
print("Number of CV Scores used in Average: ", len(scores))
print("\n\n")

# --------------------- DECISION TREE Mod --------------------- #

time1 = time.time()

mod_model_dt = DecisionTreeClassifier(splitter="random", max_depth=200, min_samples_leaf=10, max_features="log2", criterion="entropy")
mod_model_dt.fit(X_train, y_train)
mod_model_dt.score(X_test, y_test)

y_pred = mod_model_dt.predict(X_test)

time2 = time.time()

# Evaluate the model
print("\nDecision Tree Mod ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", mod_model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))
print("\nClassification report:\n\n", classification_report(y_test, y_pred))


# --------------------- DECISION TREE grid search --------------------- #

print("\nDecision Tree grid Search ---------------------\n")

grid_model_dt = DecisionTreeClassifier()
param_grid = {
    'splitter': ['best', 'random'],
    'max_depth': [None, 10, 50, 100, 200],
    'min_samples_leaf': [1, 5, 10, 20],
    'max_features': [1, 5, 10, 'sqrt', 'log2'],
    'criterion': ['gini', 'entropy']
}
grid_search = GridSearchCV(
    estimator=grid_model_dt,
    param_grid=param_grid,
    scoring="accuracy",
    cv=5,
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

best_score = grid_search.best_score_
best_param = grid_search.best_params_
best_model = grid_search.best_estimator_

# Evaluate the best model individually
print("\nbest param: ", best_param)
print("best model: ", best_model)
print("best score: ", best_score)
print("")

time1 = time.time()

best_model_dt = DecisionTreeClassifier(**best_model.get_params())
best_model_dt.fit(X_train, y_train)
y_pred = best_model_dt.predict(X_test)

time2 = time.time()

print("\nDecision Tree with best parameter ---------------------\n")
print("Time spent: ", time2 - time1)
print("\nAccuracy: ", best_model_dt.score(X_test, y_test))
print("Precision: ", metrics.precision_score(y_test, y_pred))
print("Recall: ", metrics.recall_score(y_test, y_pred))
print("F1 Score: ", metrics.f1_score(y_test, y_pred))
print("\nConfusion Matrix:\n\n", pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted']))
print("\nClassification report:\n\n", classification_report(y_test, y_pred))

#-----

cross_val_scores = cross_val_score(best_model, X_train, y_train, scoring='accuracy', cv=5)
average_precision = cross_val_scores.mean()

best_model.fit(X_train, y_train)
y_pred = best_model.predict(X_test)

#show
results = grid_search.cv_results_
precision_scores = results['mean_test_score']

plt.figure(figsize=(10, 6))
sns.heatmap(precision_scores.reshape(len(param_grid['max_depth']), -1), 
            annot=True, fmt='.4f', cmap='YlGnBu',
            xticklabels=param_grid['min_samples_leaf'],
            yticklabels=param_grid['max_depth'])
plt.xlabel('min_samples_leaf')
plt.ylabel('max_depth')
plt.title('Grid Search accuracy Scores')
plt.show()



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
