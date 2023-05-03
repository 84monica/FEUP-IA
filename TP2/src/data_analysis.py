import pandas as pd
<<<<<<< HEAD
import numpy as np

heart_disease = pd.read_csv('/home/monica/Desktop/IA/proj/FEUP-IA/TP2/dataset/Heart_Disease.csv')

for column in heart_disease.columns:
    print(f"{column}: {heart_disease[column].unique()}")
 

# initially there is no missing value
# remove the impossible values (0.0) from the heart_disease database

#heart_disease['PhysicalHealth'] = heart_disease['PhysicalHealth'].replace(0.0, np.nan)
#heart_disease['MentalHealth'] = heart_disease['MentalHealth'].replace(0.0, np.nan)
#heart_disease = heart_disease.dropna()

# check and remove duplicates:

duplicate_mask = heart_disease.duplicated()
heart_disease = heart_disease.drop_duplicates()
print(heart_disease)



=======
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../dataset/Heart Disease.csv')

# --------------------- CLASS DISTRIBUTION --------------------- #

sns.countplot(x='HeartDisease', data=dataset)
plt.title('Class Distribution')
plt.show()


# --------------------- PLOTS TO CHECK INCONSISTENCIES --------------------- #

sns.countplot(x='AlcoholDrinking', data=dataset)
plt.title('AlcoholDrinking')
plt.show()

sns.countplot(x='Sex', data=dataset)
plt.title('Sex')
plt.show()

sns.countplot(x='Stroke', data=dataset)
plt.title('Stroke')
plt.show()

sns.countplot(x='Smoking', data=dataset)
plt.title('Smoking')
plt.show()

sns.countplot(x='AgeCategory', data=dataset)
plt.title('Class Distribution')
plt.show()

sns.countplot(x='Race', data=dataset)
plt.title('Class Distribution')
plt.show()

sns.countplot(x='Diabetic', data=dataset)
plt.title('Class Distribution')
plt.show()

sns.countplot(x='GenHealth', data=dataset)
plt.title('Class Distribution')
plt.show()

# --------------------- PLOTS WITH TARGET VARIABLE --------------------- #

# SMOKERS VS. NON-SMOKERS

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['Smoking', 'HeartDisease']]

# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(
    ['Smoking', 'HeartDisease']).size().reset_index(name='Counts')

# Create grouped bar plot
sns.barplot(x="Smoking", y="Counts", hue="HeartDisease", data=grouped_data)

# Add labels
plt.title('Smoking Status and Heart Disease')
plt.xlabel('Smoking Status')
plt.ylabel('Count')

# Display plot
plt.show()

# ALCOHOL CONSUMPTION VS. HEART DISEASE

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['AlcoholDrinking', 'HeartDisease']]

# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(
    ['AlcoholDrinking', 'HeartDisease']).size().reset_index(name='Counts')

# Create grouped bar plot
sns.barplot(x="AlcoholDrinking", y="Counts",
            hue="HeartDisease", data=grouped_data)

# Add labels
plt.title('Alcohol Drinking Status and Heart Disease')
plt.xlabel('Alcohol Drinking Status')
plt.ylabel('Count')

# Display plot
plt.show()

# STROKE VS. HEART DISEASE

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['Stroke', 'HeartDisease']]

# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(
    ['Stroke', 'HeartDisease']).size().reset_index(name='Counts')

# Create grouped bar plot
sns.barplot(x="Stroke", y="Counts", hue="HeartDisease", data=grouped_data)

# Add labels
plt.title('Stroke and Heart Disease')
plt.xlabel('Stroke Status')
plt.ylabel('Count')

# Display plot
plt.show()

# DIFFICULTY WALKING VS. HEART DISEASE

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['DiffWalking', 'HeartDisease']]

# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(
    ['DiffWalking', 'HeartDisease']).size().reset_index(name='Counts')

# Create grouped bar plot
sns.barplot(x="DiffWalking", y="Counts", hue="HeartDisease", data=grouped_data)

# Add labels
plt.title('DiffWalking and Heart Disease')
plt.xlabel('DiffWalking Status')
plt.ylabel('Count')

# Display plot
plt.show()

# SEX VS. HEART DISEASE

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['Sex', 'HeartDisease']]

# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(
    ['Sex', 'HeartDisease']).size().reset_index(name='Counts')

# Create grouped bar plot
sns.barplot(x="Sex", y="Counts", hue="HeartDisease", data=grouped_data)

# Add labels
plt.title('Sex and Heart Disease')
plt.xlabel('Sex Status')
plt.ylabel('Count')

# Display plot
plt.show()
>>>>>>> 5410f098583d2cd2431cf9968d21cc71f56f0a5b
