import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')


# Visualisasi the distribution of customers around the region 
plt.figure(figsize=(10,6))
plt.hist(dataset['Region'], color='lightblue')
plt.title('Distrubusion Pelanggan Berdasarkan Wilayah', fontsize=14)
plt.xlabel('Wilayah', fontsize=14)
plt.show()