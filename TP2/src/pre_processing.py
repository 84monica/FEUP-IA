import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../dataset/Heart Disease.csv')

# --------------------- CLEAN DATASET --------------------- #

# TODO
# Physical Mental Health seems weird
# Too many age categories could be a problem
# Diabetic has more than 2 classes (could be a probem) 

# --------------------- TRANSFORM CATEGORICAL FEATURES TO NUMERIC --------------------- #

# TODO

# --------------------- CORRELATION MATRIX --------------------- #
corr_matrix = dataset.corr(method='spearman')
print(corr_matrix)

# Plot the correlation matrix using seaborn heatmap function
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True)
plt.title('Correlation Matrix')
plt.show()