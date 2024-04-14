import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Membaca dataset
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')

encoder = OneHotEncoder()
encoded_feature = encoder.fit_transform(dataset[['Month', 'VisitorType']])
# menggabungkan dataset yg sudah di encode dengan dataset asli
dataset_new = pd.concat([dataset.drop(columns=['Month', 'VisitorType']), pd.DataFrame(encoded_feature.toarray())], axis=1)


# Mengisi missing values dengan rata-rata
dataset_new.fillna(dataset_new.mean(), inplace=True)

from sklearn.preprocessing import MinMaxScaler  
#Define MinMaxScaler as scaler  
scaler = MinMaxScaler()  
#list all the feature that need to be scaled  
scaling_column = ['Administrative', 'Administrative_Duration', 'Informational', 'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues']
#Apply fit_transfrom to scale selected feature  
dataset_new[scaling_column] = scaler.fit_transform(dataset_new[scaling_column])
#Cheking min and max value of the scaling_column
print(dataset_new[scaling_column].describe().T[['min','max']])