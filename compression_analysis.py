from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVR
import time

import matplotlib.pyplot as plt
import pandas as pd


def train_models():
    data = pd.read_csv('compression_times.csv')

    le = LabelEncoder()
    data['compression_type'] = le.fit_transform(data['compression_type'])
    data['single_file'] = le.fit_transform(data['single_file'])

    X = data[['file_size', 'compression_type', 'single_file']]
    # y = data[['compression_time', 'compression_ratio']]
    y = data['compression_time']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model_kneighbors = make_pipeline(StandardScaler(),
                                     KNeighborsRegressor(n_neighbors=6))
    model_kneighbors.fit(X_train, y_train)
    print("kneighbors train:", model_kneighbors.score(X_train, y_train))
    print("kneighbors test:", model_kneighbors.score(X_test, y_test))

    model_random_forest = RandomForestRegressor(n_estimators=50, max_depth=6)
    model_random_forest.fit(X_train, y_train)
    print("random forest train:", model_random_forest.score(X_train, y_train))
    print("random forest test:", model_random_forest.score(X_test, y_test))

    model_mlp =make_pipeline(StandardScaler(), 
                             MLPRegressor(hidden_layer_sizes=(10,), activation='logistic', max_iter=10000, solver='lbfgs'))
    model_mlp.fit(X_train, y_train)
    print("mlp train:", model_mlp.score(X_train, y_train))
    print("mlp test:", model_mlp.score(X_test, y_test))


train_models()
