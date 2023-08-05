from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import os

import pandas as pd


def train_models():
    data = pd.read_csv('compression_times.csv')

    le = LabelEncoder()
    data['compression_type'] = le.fit_transform(data['compression_type'])
    data['storage_type'] = le.fit_transform(data['storage_type'])
    data['file_type'] = le.fit_transform(data['file_type'])

    X = data[['file_size', 'compression_type', 'storage_type', 'file_type']]
    y = data[['compression_time', 'compression_ratio', 'decompression_time']]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model_random_forest = RandomForestRegressor(n_estimators=100, max_depth=13)
    model_random_forest.fit(X_train.values, y_train)
    # print("random forest train:", model_random_forest.score(X_train, y_train))
    # print("random forest test:", model_random_forest.score(X_test, y_test))

    # kneighbors and mlp are commented because they are not as accurate
    # as random forest, but we left them in because we reference them in the
    # report

    # model_kneighbors = make_pipeline(StandardScaler(),
    #                                  KNeighborsRegressor(n_neighbors=10))
    # model_kneighbors.fit(X_train, y_train)
    # print("kneighbors train:", model_kneighbors.score(X_train, y_train))
    # print("kneighbors test:", model_kneighbors.score(X_test, y_test))
    # model_mlp = make_pipeline(StandardScaler(),
    #                           MLPRegressor(hidden_layer_sizes=(8,), activation='logistic', max_iter=10000, solver='lbfgs'))
    # model_mlp.fit(X_train, y_train)
    # print("mlp train:", model_mlp.score(X_train, y_train))
    # print("mlp test:", model_mlp.score(X_test, y_test))

    # return model_kneighbors, model_random_forest, model_mlp
    return model_random_forest


# model_kneighbors, model_random_forest, model_mlp = train_models()


def predict_compression_alg(file_type, file_size, model, storage_type):
    compression_types = {'zlib': 0, 'gzip': 1,
                         'bz2': 2, 'lzma': 3, 'zipfile': 4, 'tarfile': 5}
    min_compression_time = float("inf")
    min_compression_time_type = None
    min_compression_time_y = None
    max_compression_ratio = float("-inf")
    max_compression_ratio_type = None
    max_compression_ratio_y = None

    for compression_type, value in compression_types.items():
        X = [[file_size, value, file_type, storage_type]]
        y = model.predict(X)
        if y[0][0] < min_compression_time:
            min_compression_time = y[0][0]
            min_compression_time_type = compression_type
            min_compression_time_y = y
        if y[0][1] > max_compression_ratio:
            max_compression_ratio = y[0][1]
            max_compression_ratio_type = compression_type
            max_compression_ratio_y = y

    return (min_compression_time_type, min_compression_time_y), (max_compression_ratio_type, max_compression_ratio_y)


def make_predictions(model, storage_type):
    file_types = {'csv': 0, 'file': 1, 'json': 2, 'txt': 3}
    predictions = []
    data_files = ['test/' + file for file in os.listdir('test')]
    for file in data_files:
        file_size = os.path.getsize(file)
        file_type = file.split('.')[-1]
        file_type = file_types[file_type]
        min_time_tuple, max_ratio_tuple = predict_compression_alg(
            file_type, file_size, model, storage_type)
        min_time_compression = min_time_tuple[0]
        min_time_time = min_time_tuple[1][0][0]
        min_time_ratio = min_time_tuple[1][0][1]
        max_ratio_compression = max_ratio_tuple[0]
        max_ratio_time = max_ratio_tuple[1][0][0]
        max_ratio_ratio = max_ratio_tuple[1][0][1]
        predictions.append((file, min_time_compression, min_time_time, min_time_ratio,
                            max_ratio_compression, max_ratio_time, max_ratio_ratio))
    df = pd.DataFrame(predictions, columns=[
                      'file', 'min_time_compression_type', 'min_time_compression_time',
                      'min_time_compression_ratio', 'max_ratio_compression_type',
                      'max_ratio_compression_time', 'max_ratio_compression_ratio'])
    df.to_csv('test/predictions.csv')


def main():
    storage_type = input("HDD: 0, SSD: 1, NVMe: 2 \nEnter storage type: ")
    random_forest_model = train_models()
    make_predictions(random_forest_model, storage_type)


if __name__ == "__main__":
    main()
