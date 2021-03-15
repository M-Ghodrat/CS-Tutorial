import numpy as np
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score
from predict import *

df = pd.read_csv("/home/mgh/CS-Tutorial/Extra/KNN/dataset/new_MinMaxScaled.csv")

label = 'regime'
index_label = 'Unnamed: 0'

test_size = 0.20
Data = Dataset(dataframe=df, label=label, test_size=test_size)

n_neighbors = 5
# weights = 'uniform'
weights = 'distance'
knn = KNN(dataset=Data, n_neighbors=n_neighbors, weights = weights)

print(f"Confusion_matrix_train for k={n_neighbors}, weights={weights}:", knn.train_confusion_matrix)
print(f"Confusion_matrix_test for k={n_neighbors}, weights={weights}:", knn.test_confusion_matrix)
print(f"Classification_report_train for k={n_neighbors}, weights={weights}:", knn.train_classification_report)
print(f"Classification_report_test for k={n_neighbors}, weights={weights}:", knn.test_classification_report)
print(f"Accuracy_score_train for k={n_neighbors}, weights={weights}:", knn.train_accuracy_score)
print(f"Accuracy_score_test for k={n_neighbors}, weights={weights}:", knn.test_accuracy_score)
print(f"Precision_score_train for k={n_neighbors}, weights={weights}:" , knn.train_precision_score)
print(f"Precision_score_test for k={n_neighbors}, weights={weights}:" , knn.test_precision_score)
print(f"F1_score_train for k={n_neighbors}, weights={weights}:" , knn.train_f1_score)
print(f"F1_score_test for k={n_neighbors}, weights={weights}:" , knn.test_f1_score)

plot_confusion_matrix(knn.knn_model, Data.feature_test, Data.label_test)
