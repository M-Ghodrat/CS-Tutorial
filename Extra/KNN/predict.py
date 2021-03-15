from sklearn.neighbors import KNeighborsClassifier
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score

class Dataset:
    def __init__(self, dataframe, label, test_size):
        self.label = dataframe[label]
        data_feature = list(dataframe.columns)
        data_feature.remove(self.label.name)
        data_feature.remove('Unnamed: 0')
        self.feature = dataframe[data_feature]
        self.feature_train, self.feature_test, self.label_train, self.label_test = model_selection.train_test_split(self.feature, self.label, test_size=test_size)

class KNN:
    def __init__(self, dataset, n_neighbors, weights):

        #Building a k-NN QuAM
        self.knn_model = KNeighborsClassifier(n_neighbors=n_neighbors, weights = weights)
        self.knn_model.fit(dataset.feature_train,dataset.label_train)

        # prediction
        self.train = self.knn_model.predict(dataset.feature_train)
        self.test = self.knn_model.predict(dataset.feature_test)

        # Accuracy scores
        self.train_accuracy_score = accuracy_score(dataset.label_train, self.train)
        self.test_accuracy_score = accuracy_score(dataset.label_test, self.test)

        # confusion matrices
        self.train_confusion_matrix = confusion_matrix(dataset.label_train, self.train)
        self.test_confusion_matrix = confusion_matrix(dataset.label_test, self.test)

        # classification reports
        self.train_classification_report = classification_report(dataset.label_train, self.train)
        self.test_classification_report = classification_report(dataset.label_test, self.test)

        # Precision scores
        self.train_precision_score = precision_score(dataset.label_train, self.train, average='weighted')
        self.test_precision_score = precision_score(dataset.label_test, self.test, average='weighted')

        # F1 scores
        self.train_f1_score = f1_score(dataset.label_train, self.train, average='weighted')
        self.test_f1_score = f1_score(dataset.label_test, self.test, average='weighted')



