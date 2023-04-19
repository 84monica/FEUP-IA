import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('../dataset/Heart Disease.csv')


# DATA ANALYSIS WITH TARGET VARIABLE



# SMOKERS VS. NON-SMOKERS

# Create a new DataFrame with smoker and heart disease columns
smoker_heartdisease = dataset[['Smoking', 'HeartDisease']]
 
# Count instances of smoker and heart disease grouping
grouped_data = smoker_heartdisease.groupby(['Smoking', 'HeartDisease']).size().reset_index(name='Counts')
 
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
grouped_data = smoker_heartdisease.groupby(['AlcoholDrinking', 'HeartDisease']).size().reset_index(name='Counts')
 
# Create grouped bar plot
sns.barplot(x="AlcoholDrinking", y="Counts", hue="HeartDisease", data=grouped_data)
 
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
grouped_data = smoker_heartdisease.groupby(['Stroke', 'HeartDisease']).size().reset_index(name='Counts')
 
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
grouped_data = smoker_heartdisease.groupby(['DiffWalking', 'HeartDisease']).size().reset_index(name='Counts')
 
# Create grouped bar plot
sns.barplot(x="DiffWalking", y="Counts", hue="HeartDisease", data=grouped_data)
 
# Add labels
plt.title('DiffWalking and Heart Disease')
plt.xlabel('DiffWalking Status')
plt.ylabel('Count')
 
# Display plot
plt.show()

# TODO
# 1. Plot with BMI and Heart Disease
# 2. Plot with Age and Heart Disease
# 3. Plot with Physical Health and Heart Disease
# 4. Plot with Mental Health and Heart Disease
# 5. Plot with Sex and Heart Disease
# ...