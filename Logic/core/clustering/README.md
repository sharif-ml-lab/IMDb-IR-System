# Clustering

This folder contains Python classes for clustering and analyzing your data. You can add additional functions or minor alternations if needed, but do not delete any existing functions.

**Important Notes:**

- We are using **Weights & Biases (WandB)** for visualization, which is an excellent way to share and visualize your plots and data.
- You need to create and log your plots in WandB. Once logged, they can be added to a report.
- After creating a report, you can share it with others by copying the **magic link**. Users with the magic link do not need to log into WandB to view the report.

## Classes

### 1. [Clustering Utils](./clustering_utils.py)
- This class contains all the necessary utilities and functions for performing clustering.
- It includes functions to implement clustering methods (**K-Means**, **Hierarchical**) and visualize each method or additional techniques like the **elbow method** for visualization.

### 2. [Clustering Metrics](./clustering_metrics.py)
- This class calculates clustering metrics, such as the adjusted Rand score, which you can call in the main function to evaluate your results.

### 3. [Dimension Reduction](./dimension_reduction.py)
- As we are working with high-dimensional data, it is necessary to perform **PCA** on our embeddings to work with useful information and data only.
- Along with PCA, we have **2D t-SNE**, which will be helpful in plotting the clusterings.

### 4. [Main](./main.py)
- This is the main function where you need to call all the functions from the previously mentioned classes to evaluate how well you can cluster (by examining the metrics and visualizations).
- Ensure that the implemented functions work correctly by calling them in the main class.
- Some functions are already called in the given main class, but make sure to call the rest with different values for ranges, linkage methods, etc., in the main class as well.