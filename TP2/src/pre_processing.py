import pandas as pd

dataset = pd.read_csv('../dataset/Heart_Disease.csv')

# --------------------- CLEAN DATASET --------------------- #

# Check and remove duplicates
count_before = len(dataset)
print("row count (before) is: ", count_before)
dataset = dataset.drop_duplicates()
count_after = len(dataset)
print("row count (after) is: ", count_after)
print("number of duplicates: ", count_before-count_after)
print("")

# --------------------- HANDLING CATEGORICAL FEATURES --------------------- #

# One-Hot Encoding for categorical features
dataset = pd.get_dummies(dataset, columns = ["Race", "AgeCategory","Smoking","AlcoholDrinking","Stroke","DiffWalking","Sex","Diabetic","PhysicalActivity","GenHealth","Asthma","KidneyDisease","SkinCancer"])

# Change target variable to binary values
d = {'Yes': 1, 'No': 0}
dataset['HeartDisease'] = dataset['HeartDisease'].map(d)

# --------------------- CORRELATION MATRIX --------------------- #

# Correlation matrix only with target variable
corr_matrix = dataset.corr(method='spearman')
#print("Correlation Method : spearman\n",corr_matrix)
corr_matrix = corr_matrix.loc[['HeartDisease']]
#print("Loc HeartDisease\n", corr_matrix)
corr_matrix = corr_matrix.drop(['HeartDisease'], axis=1)
print("Corrlation for HeartDisease\n", corr_matrix)

# --------------------- FEATURE SELECTION --------------------- #

# Drop features with low correlation
treshold = 0.12
corr_matrix = corr_matrix.loc[:, (abs(corr_matrix) > treshold).any()]
features_corr = list(corr_matrix.columns)
dataset = dataset[['HeartDisease'] + features_corr]
print("\nColumns with high Correlation (>",treshold, "): \n", features_corr)

# Save dataset
dataset.to_csv('../dataset/Heart_Disease_Processed.csv', index=False)
