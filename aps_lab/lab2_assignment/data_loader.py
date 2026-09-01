import pandas as pd
from sklearn.datasets import load_breast_cancer


def load_dataset():

    data = load_breast_cancer()

    X = pd.DataFrame(
        data.data,
        columns=data.feature_names
    )

    y = pd.Series(
        (data.target == 0).astype(int),
        name="malignant"
    )

    return data, X, y
