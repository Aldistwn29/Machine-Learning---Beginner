import pandas as pd
dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')

# Data Pre-processing : heandling missing value part1

#checking missing value for each feature  
print('Checking missing value for each feature:')
print(dataset.isnull().sum())
#Counting total missing value
print('\nCounting total missing value:')
print(dataset.isnull().sum().sum())

# part 2
#Drop rows with missing value   
dataset_clean = dataset.dropna().shape  
print('\nUkuran dataset_clean:', dataset_clean)
