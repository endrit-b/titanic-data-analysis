import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

X = np.array([[1, 2],
              [5, 8],
              [1.5, 1.8],
              [8, 8],
              [1, 0.6],
              [9, 11]])

plt.scatter(X[:, 0], X[:, 1], s=150)
plt.show()

colors = 10 * ['g', 'r', 'c', 'b', 'k']


class KMeansClustering:

    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
        self.centroids = {}
        self.classifications = {}

    def fit(self, data):
        self.centroids = {}

        for i in range(self.k):
            self.centroids[i] = data[i]

        for i in range(self.max_iter):
            self.classifications = {}

            for j in range(self.k):
                self.classifications[j] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset - self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
            prev_centorids = dict(self.centroids)

            for classification in self.classifications:
                # self.centroids[classification] = np.average(self.classifications[classification], axis=0)
                pass

            optimized = True

            for c in self.centroids:
                original_centroid = prev_centorids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid - original_centroid)/original_centroid * 100.0) > self.tol:
                    optimized = False

            if optimized:
                break


    def predict(self, data):
        distances = [np.linalg.norm(data - self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))

        return classification

clf = KMeansClustering()

clf.fit(X)

for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0], clf.centroids[centroid][1], marker='o', color='k', s=150, linewidths=5)


for classification in clf.classifications:
    color = colors

    for featureset in clf.classifications[classification]:
        plt.scatter(featureset[0], featureset[1], marker='x', color=colors, s=150, linewidths=5)

plt.show()