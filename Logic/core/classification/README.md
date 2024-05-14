# Classification

This package contains the code for the classification phase of the project.
The classification phase is responsible for classifying the comment data into two classes: positive and negative.
you have to train the models on the training data and then use the trained model to classify the comment data which you crawled in the first phase. You can access the training data using [this link](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews/code).

## Classes

Here is a brief description of the files in this package:

### 1. [Basic Classifier](basic_classifier.py)
This file contains a abstract class `BasicClassifier` which is the base class for all the classifiers in this package. You should implement function `get_percent_of_positive_reviews` in this class which is responsible to compute percentage of positive reviews of a list of reviews. In all classifiers, you have to use the fasttext embeddings as the input to the classifier except for the Naive Bayes classifier. In the Naive Bayes classifier, you have to use the count vectorizer to convert the text data into the input for the classifier.

### 2. [Naive Bayes](naive_bayes.py)
This file contains the implementation of the Naive Bayes classifier.

### 3. [SVM](svm.py)
This file contains the implementation of the Support Vector Machine classifier. you can use the sci-kit learn library to implement the SVM classifier.

### 4. [KNN](knn.py)
This file contains the implementation of the K-Nearest Neighbors classifier.

### 5. [Deep Model](deep.py)
This file contains the implementation of the MLP model using the PyTorch library.

### 6. [Data Loader](data_loader.py)
This file contains the implementation of the data loader class which is responsible for loading the data from the disk and use fasttext model to generate the word embeddings. you have to split the data into training and testing data in this file.
