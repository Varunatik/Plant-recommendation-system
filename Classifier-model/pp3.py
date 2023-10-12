# Importing the libraries
import urllib
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import csv
import requests


# Importing the dataset
dataset = pd.read_csv('dataset1.csv')
dataset2 = pd.read_csv('dataset2.csv')

print("\nHead________________________________________________________")
print(dataset.head())
print("\nDesription________________________________________________________")
print(dataset.describe())

# Preprocessing
print("\nNull Values________________________________________________________")
print(dataset.isnull().sum())

# Splitting the dataset into the X and Y
x = dataset.iloc[:, 2:6].values
y = dataset.iloc[:, 6].values

# Splitting the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)
print("\nTrain________________________________________________________")
print(x_train)
print(y_train)
print("\nTest________________________________________________________")
print(x_test)
print(y_test)

#Forr testing the algorithm
t1clas=dataset[dataset["Temperature LL"] <= 20]
tclas=t1clas[t1clas["Temperature UL"] >= 20]
h1tclas=tclas[tclas["Humidity LL"] <= 97]
htclas=h1tclas[h1tclas["Humidity UL"] >= 97]

print("\nPlants_______________________________________________________")
print(htclas)

#For testing algorithm on merged data
df1=pd.DataFrame(dataset, columns=['Plants', 'Humidity UL', 'Humidity LL', 'Temperature UL', 'Temperature LL'] )
df2=pd.DataFrame(dataset2, columns=['Plants', 'Soil preperation', 'Germination', 'Water req.', 'Compost Req.', 'Pot size', 'Uses', 'Timeline', 'Special Care Points'])
merged=pd.merge(df1, df2, how='left', on=['Plants', 'Plants'])

t2clas=merged[merged["Temperature LL"] <= 20]
t3clas=t2clas[t2clas["Temperature UL"] >= 20]
h2tclas=t3clas[t3clas["Humidity LL"] <= 97]
h0tclas=h2tclas[h2tclas["Humidity UL"] >= 97]

print("\n\nPlant Description_____________________________________________")
print(h0tclas)

#Actual implementation of the algorithm
#reading sensor data from exported csv files
df3=pd.read_csv('1.csv')
df4=pd.read_csv('2.csv')
a=df3.iloc[2]['field1']
b=df4.iloc[2]['field2']

#actual implementation of algorithm
t10clas=dataset[dataset["Temperature LL"] <= a]
t0clas=t10clas[t10clas["Temperature UL"] >= a]
h1t0clas=t0clas[t0clas["Humidity LL"] <= b]
ht0clas=h1t0clas[h1t0clas["Humidity UL"] >= b]

print("\nPlants_______________________________________________________")
print(ht0clas)

#merging the dataset and application of algorithm
df1=pd.DataFrame(dataset, columns=['Plants', 'Humidity UL', 'Humidity LL', 'Temperature UL', 'Temperature LL'] )
df2=pd.DataFrame(dataset2, columns=['Plants', 'Soil preperation', 'Germination', 'Water req.', 'Compost Req.', 'Pot size', 'Uses', 'Timeline', 'Special Care Points'])
merged=pd.merge(df1, df2, how='left', on=['Plants', 'Plants'])

t20clas=merged[merged["Temperature LL"] <= a]
t30clas=t20clas[t20clas["Temperature UL"] >= a]
h2t0clas=t30clas[t30clas["Humidity LL"] <= b]
h0t0clas=h2t0clas[h2t0clas["Humidity UL"] >= b]

print("\n\nPlant Description_____________________________________________")
print(h0t0clas)
