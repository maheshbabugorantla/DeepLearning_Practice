import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit

def main():

    X = np.array([1, 2, 3, 4, 5, 6, 7, 8]) #, [3, 4], [1, 2], [3, 4]])
    y = np.array([0, 0, 1, 1, 1, 1, 0, 0])

    sss = StratifiedShuffleSplit(n_splits=1, test_size=0.2) #, random_state=0)
    print(sss.get_n_splits())
    print(sss)

    print(next(sss.split(X, y)))
    print(next(sss.split(X, y)))
    print(next(sss.split(X, y)))
    print(next(sss.split(X, y)))

    # for train_index, test_index in sss.split(X, y):
    #     print("TRAIN:", train_index, "TEST:", test_index)
    #     X_train, X_test = X[train_index], X[test_index]
    #     y_train, y_test = y[train_index], y[test_index]

if __name__ == '__main__':
    main()
