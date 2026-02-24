import numpy as np
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression

class AnalyticsEngine:

    def clustering(self, data):
        model = KMeans(n_clusters=3, random_state=42)
        labels = model.fit_predict(data)
        return labels.tolist()

    def prediction(self, X, y):
        model = LinearRegression()
        model.fit(X, y)
        return model.predict(X).tolist()

    def anomaly_detection(self, data):
        data = np.array(data)
        mean = np.mean(data)
        std = np.std(data)
        threshold = mean + 2 * std
        anomalies = data[data > threshold]
        return anomalies.tolist()
