import numpy as np
import os
from tqdm import tqdm
from sklearn.model_selection import train_test_split

from ..word_embedding.fasttext_data_loader import FastTextDataLoader
from ..word_embedding.fasttext_model import FastText
from .dimension_reduction import DimensionReduction
from .clustering_metrics import ClusteringMetrics
from .clustering_utils import ClusteringUtils

# Main Function: Clustering Tasks

# 0. Embedding Extraction
# TODO: Using the previous preprocessor and fasttext model, collect all the embeddings of our data and store them.

# 1. Dimension Reduction
# TODO: Perform Principal Component Analysis (PCA):
#     - Reduce the dimensionality of features using PCA. (you can use the reduced feature afterward or use to the whole embeddings)
#     - Find the Singular Values and use the explained_variance_ratio_ attribute to determine the percentage of variance explained by each principal component.
#     - Draw plots to visualize the results.

# TODO: Implement t-SNE (t-Distributed Stochastic Neighbor Embedding):
#     - Create the convert_to_2d_tsne function, which takes a list of embedding vectors as input and reduces the dimensionality to two dimensions using the t-SNE method.
#     - Use the output vectors from this step to draw the diagram.

# 2. Clustering
## K-Means Clustering
# TODO: Implement the K-means clustering algorithm from scratch.
# TODO: Create document clusters using K-Means.
# TODO: Run the algorithm with several different values of k.
# TODO: For each run:
#     - Determine the genre of each cluster based on the number of documents in each cluster.
#     - Draw the resulting clustering using the two-dimensional vectors from the previous section.
#     - Check the implementation and efficiency of the algorithm in clustering similar documents.
# TODO: Draw the silhouette score graph for different values of k and perform silhouette analysis to choose the appropriate k.
# TODO: Plot the purity value for k using the labeled data and report the purity value for the final k. (Use the provided functions in utilities)

## Hierarchical Clustering
# TODO: Perform hierarchical clustering with all different linkage methods.
# TODO: Visualize the results.

# 3. Evaluation
# TODO: Using clustering metrics, evaluate how well your clustering method is performing.
