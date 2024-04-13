import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.impute import SimpleImputer

# Persiapan Data
dataset = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv")

# Mengubah kolom kategorikal menjadi one-hot encoding
dataset = pd.get_dummies(dataset, drop_first=True)

# Membagi dataset menjadi data latih dan data uji
X = dataset.drop(['Revenue'], axis=1)
y = dataset['Revenue']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Mengisi nilai NaN dengan mean dari kolom tersebut
imputer = SimpleImputer(strategy='mean')
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Melakukan standarisasi fitur
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Membuat model Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Memprediksi hasil test set
y_pred = model.predict(X_test)

# Menampilkan confusion matrix dan classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
