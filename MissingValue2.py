import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')


print("Before imputation:")
# Checking missing value for each feature  
print(dataset.isnull().sum())
# Counting total missing value  
print(dataset.isnull().sum().sum())

# Konversi nilai ke tipe data numerik
dataset['Month'] = pd.to_numeric(dataset['Month'], errors='coerce')
dataset['VisitorType'] = pd.to_numeric(dataset['VisitorType'], errors='coerce')

# Menggunakan concat
dataset_new = pd.concat([dataset, dataset['Month'], dataset['VisitorType']], axis=1)
dataset_new = dataset_new.drop(['Month', 'VisitorType'], axis=1)

print("\nAfter imputation:")
# Fill missing value with mean of feature value
dataset_new.fillna(dataset_new.mean(), inplace = True)
# Checking missing value for each feature  
print(dataset_new.isnull().sum())
# Counting total missing value  
print(dataset_new.isnull().sum().sum())