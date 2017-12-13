from os.path import join, dirname
from load_data import load_dataset
from model import classify
import languageflow
from languageflow.log import MultilabelLogger

data_file = join(dirname(dirname(dirname(__file__))), "data", "fb_bank_category",
                 "corpus", "test.xlsx")
X_test, y_test = load_dataset(data_file)
y_test = [tuple(item) for item in y_test]
y_pred = classify(X_test)

log_folder = join(dirname(__file__), "analyze")
MultilabelLogger.log(X_test, y_test, y_pred, folder=log_folder)
languageflow.board(log_folder)
