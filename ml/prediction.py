import numpy as np
from sklearn.linear_model import LinearRegression

def predict_future(cum_growth, store_IDs):
    predictions = []

    for i in range(len(store_IDs)):
        X = np.array([1, 2, 3, 4]).reshape(-1, 1)
        y = cum_growth[i]

        model = LinearRegression()
        model.fit(X, y)

        pred = model.predict([[5]])
        predictions.append(pred[0])

    future_best = np.argmax(predictions)
    
    return predictions, future_best
