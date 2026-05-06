import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

# Load dataset
df = pd.read_csv('https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv', skipinitialspace=True)
x_cols = [c for c in df.columns if c != 'income']
X = df[x_cols]
y = df['income']
print("First 5 rows of data:")
print(df.head())
print("\nDataset shape:", df.shape)

# Data split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1234)

# Fill missing values
train_mode = dict(X_train.mode().iloc[0])
X_train = X_train.fillna(train_mode)
print("\nTrain mode values for missing data:")
print(train_mode)

# Convert categoricals
encoders = {}
for column in ['workclass', 'education', 'marital-status',
               'occupation', 'relationship', 'race',
               'sex', 'native-country']:
    categorical_convert = LabelEncoder()
    X_train[column] = categorical_convert.fit_transform(X_train[column])
    encoders[column] = categorical_convert

# Train models
print("\nTraining Random Forest...")
rf = RandomForestClassifier(n_estimators=100)
rf = rf.fit(X_train, y_train)

print("Training Extra Trees...")
et = ExtraTreesClassifier(n_estimators=100)
et = et.fit(X_train, y_train)

# Save models and preprocessing
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(et, "./extra_trees.joblib", compress=True)
print("\nSuccessfully saved all models and preprocessing artifacts!")
