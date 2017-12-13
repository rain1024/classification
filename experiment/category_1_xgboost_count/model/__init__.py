import joblib
from os.path import join, dirname
import sys

sys.path.insert(0, dirname(__file__))

y_transform = joblib.load(join(dirname(__file__), "label.transformer.bin"))
x_transform = joblib.load(join(dirname(__file__), "count.transformer.bin"))
estimator = joblib.load(join(dirname(__file__), "model.bin"))


def classify(input):
    if not isinstance(input, list):
        X = [input]
    else:
        X = input
    X = x_transform.transform(X)
    y = estimator.predict(X)
    y = y_transform.inverse_transform(y)
    if not isinstance(input, list):
        y = y[0]
    return y