import pandas as pd
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



