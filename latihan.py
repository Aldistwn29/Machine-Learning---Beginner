import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv")

# Eksplorasi Data: Memahami Data dengan Statistik - Part 1
print('Shape dataset:', dataset.shape)
print('\nLima data teratas:\n', dataset.head())
print('\nInformasi dataset:')
print(dataset.info())
print('\nStatistik deskriptif:\n', dataset.describe())

# Eksplorasi Data: Memahami Data dengan Statistik - Part 2

# # Mengabaikan kolom non-numerik saat menghitung korelasi
data_corr = dataset.select_dtypes(include=['float64', 'int64', 'bool']).columns
dataset_corr = dataset[data_corr]
new_data_corr = dataset_corr.corr()


print('Korelasi dataset (hanya kolom numerik):\n', new_data_corr)
print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())
print('Distribusi Label (Weekend):\n', dataset['Weekend'].value_counts())

# # Tugas praktek
print('\nKorelasi BounceRates-ExitRates:', new_data_corr.loc['BounceRates','ExitRates'])
print('\nKorelasi Revenue-PageValues:', new_data_corr.loc['Revenue','PageValues'])
print('\nKorelasi TrafficType-Weekend:', new_data_corr.loc['TrafficType','Weekend'])

# Membuat visualisasi
# checking the Distribution of customers on Revenue
plt.rcParams['figure.figsize'] = (12,5)
plt.subplot(1, 2, 1)
sns.countplot(data = dataset, x='Revenue', palette='pastel')
plt.title('Buy or Not', fontsize=28)
plt.xlabel('Revenue or not', fontsize=14)
plt.ylabel('count', fontsize=14)

# checking the Distribution of customers on Weekend
plt.subplot(1, 2, 2)
sns.countplot(data= dataset, x='Weekend', palette = 'inferno')
plt.title('Purchase on Weekends', fontsize = 20)
plt.xlabel('Weekend or not', fontsize = 14)
plt.ylabel('count', fontsize = 14)
plt.show()