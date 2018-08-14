from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import metrics
from sklearn.preprocessing import normalize,scale
from sklearn.decomposition import PCA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA as sklearnPCA
from pandas.plotting import parallel_coordinates

def knn(report, sample_path='./vertebral_column_data/column_3C.dat'):
    #importing dataset and converting to datasframe
    header = ['pelvic_incidence', 'pelvic_tilt', 'lumbar_lordosis_angle', 'sacral_slope', 'pelvic_radius', 'grade_of_spondylolisthesis', 'label']
    df = pd.read_csv(sample_path, sep=' ', header=None, names=header)

    features = df.iloc[:,0:6]
    labels = df.iloc[:,6]
    model = KNeighborsClassifier(n_neighbors=5, weights='distance')
    model.fit(features,labels)

    predicted = model.predict(report)
    predicted_proba = model.predict_proba(report)

    return(predicted, predicted_proba)
