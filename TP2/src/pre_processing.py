import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../dataset/Heart_Disease.csv')

# --------------------- CLEAN DATASET --------------------- #

# check and remove duplicates
duplicate_mask = dataset.duplicated()
heart_disease = dataset.drop_duplicates()

# --------------------- HANDLING CATEGORICAL FEATURES --------------------- #

# For now removing age category
print(dataset['AgeCategory'].unique())
print(dataset['AgeCategory'].value_counts())
dataset = dataset.drop(['AgeCategory'], axis=1)

# One-Hot Encoding for categorical features
dataset = pd.get_dummies(dataset, columns = ["Smoking","AlcoholDrinking","Stroke","DiffWalking","Sex","Race","Diabetic","PhysicalActivity","GenHealth","Asthma","KidneyDisease","SkinCancer"])

# Change target variable to binary values
d = {'Yes': 1, 'No': 0}
dataset['HeartDisease'] = dataset['HeartDisease'].map(d)

# --------------------- CORRELATION MATRIX --------------------- #

corr_matrix = dataset.corr(method='spearman')
print(corr_matrix)

# Plot the correlation matrix using seaborn heatmap function
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()

# --------------------- FEATURE SELECTION --------------------- #

# Drop race column
dataset = dataset.drop(['Race'], axis=1)

# Save dataset
print(dataset)
dataset.to_csv('../dataset/Heart Disease - Processed.csv', index=False)

# --------------------- TODO LIST --------------------- #
# TODO: Target Encoding because many age categories could be a problem
# TODO: Clean correlation matrix
# TODO: Feature selection