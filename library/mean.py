# %matplotlib notebook
from itertools import cycle
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth
import numpy as np


def mean_find(data):
    
    # Convert the frame to its Numpy-array representation.
    income_numpy_matrix = data.as_matrix()
    
    print(data)
    print(income_numpy_matrix)

    def mean_shift(data, n_samples=1000):
        bandwidth = estimate_bandwidth(data, quantile=0.2, 
                                    n_samples=n_samples)

        ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
        ms.fit(data)
        labels = ms.labels_
        cluster_centers = ms.cluster_centers_

        labels_unique = np.unique(labels)
        n_clusters = len(labels_unique)

        print('Number of estimated clusters : {}'.format(n_clusters))
        
        return labels, cluster_centers, n_clusters
    
    mean_shift(income_numpy_matrix)

    def plot_income_data():
        labels, cluster_centers, n_clusters = mean_shift(income_numpy_matrix)

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # k is black.
        colors = cycle('bgrcmy')
        for k, col in zip(range(n_clusters), colors):
            my_members = (labels == k)
            cluster_center = cluster_centers[k]
            
            x, y = income_numpy_matrix[my_members,0], income_numpy_matrix[my_members,1]
            ax.scatter(x, y, c=col, linewidth=0.2)
            ax.scatter(cluster_center[0], cluster_center[1], c='k', s=50, linewidth=0.2)
            
        plt.title('Estimated number of clusters: {}'.format(n_clusters))
        plt.show()

    plot_income_data()