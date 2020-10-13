import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from .models import Profile
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from joblib import dump, load
from .my_database import DatabaseHelper

class Knn():
    def cos():
        cols = [field.name for field in Profile._meta.get_fields()]
        cols = cols[1:]
        cols.sort()
        data = DatabaseHelper.getProfiles()
        df = pd.DataFrame(data, columns=cols)
        print(df)
        print(df.describe())
        
        #sns.pairplot(df)
        #plt.show()

        #sns.heatmap(df.corr(), annot=True)

        df['class_encod'] = df['name'].apply(lambda x: 0 if x == 'Patryk' else 1 if x == 'nowy' else 2)
        df['class_encod'].unique()

        print(df.describe())
        print(df['class_encod'])

        y = df[['class_encod']] # target attributes 
        X = df.iloc[:, 0:4] # input attributes
        print(X.head())

        #X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
        #np.shape(y_train)

        #m = KNeighborsClassifier()
        #m.fit(X_train, np.ravel(y_train))

        #m.predict(X_test.iloc[0:10]) 

        #m.score(X_test, y_test)
        #confusion_matrix(y_test, m.predict(X_test))

        #dump(m, 'iris-classifier.dmp')
        #ic = load('iris-classifier.dmp')
        #confusion_matrix(y_test, ic.predict(X_test))
            