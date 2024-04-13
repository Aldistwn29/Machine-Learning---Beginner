import pandas as pd

# Membuat DataFrame contoh
df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, None],
    'C': [1, None, 3, 4]
})

# Menghapus baris yang mengandung setidaknya satu NaN
df_cleaned = df.dropna()

# Menghapus kolom yang mengandung setidaknya satu NaN
df_cleaned_columns = df.dropna(axis=1)

# Menghapus baris yang semua nilainya adalah NaN
df_cleaned_all = df.dropna(how='all')

# Menghapus baris yang memiliki kurang dari 3 nilai non-NaN
df_thresh = df.dropna(thresh=3)

# Menghapus baris berdasarkan nilai NaN di kolom tertentu
df_subset = df.dropna(subset=['A', 'C'])

print("Original DataFrame:\n", df)
print("\nDataFrame setelah dropna:\n", df_cleaned)
print("\nDataFrame setelah menghapus kolom:\n", df_cleaned_columns)
print("\nDataFrame setelah menghapus baris dengan semua NaN:\n", df_cleaned_all)
print("\nDataFrame setelah menerapkan thresh:\n", df_thresh)
print("\nDataFrame setelah menerapkan subset:\n", df_subset)

# Contoh DataFrame
import pandas as pd

df = pd.DataFrame({
    'A': [None, None, None],
    'B': [None, None, None],
    'C': [None, None, None]
})

df_cleaned = df.dropna(thresh=1)
print(df_cleaned)