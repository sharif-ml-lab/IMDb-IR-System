import numpy as np

from typing import List
from sklearn.metrics import silhouette_score
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import confusion_matrix


class ClusteringMetrics:

    def __init__(self):
        pass

    def silhouette_score(self, embeddings: List, cluster_labels: List) -> float:
        """
        Calculate the average silhouette score for the given cluster assignments.

        Parameters
        -----------
        embeddings: List
            A list of vectors representing the data points.
        cluster_labels: List
            A list of cluster assignments for each data point.

        Returns
        --------
        float
            The average silhouette score, ranging from -1 to 1, where a higher value indicates better clustering.
        """
        pass

    def purity_score(self, true_labels: List, cluster_labels: List) -> float:
        """
        Calculate the purity score for the given cluster assignments and ground truth labels.

        Parameters
        -----------
        true_labels: List
            A list of ground truth labels for each data point (Genres).
        cluster_labels: List
            A list of cluster assignments for each data point.

        Returns
        --------
        float
            The purity score, ranging from 0 to 1, where a higher value indicates better clustering.
        """
        pass

    def adjusted_rand_score(self, true_labels: List, cluster_labels: List) -> float:
        """
        Calculate the adjusted Rand index for the given cluster assignments and ground truth labels.

        Parameters
        -----------
        true_labels: List
            A list of ground truth labels for each data point (Genres).
        cluster_labels: List
            A list of cluster assignments for each data point.

        Returns
        --------
        float
            The adjusted Rand index, ranging from -1 to 1, where a higher value indicates better clustering.
        """
        pass
