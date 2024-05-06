import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from .basic_classifier import BasicClassifier
from .data_loader import ReviewLoader


class NaiveBayes(BasicClassifier):
    def __init__(self, count_vectorizer, alpha=1):
        super().__init__()
        self.cv = count_vectorizer
        self.num_classes = None
        self.classes = None
        self.number_of_features = None
        self.number_of_samples = None
        self.prior = None
        self.feature_probabilities = None
        self.log_probs = None
        self.alpha = alpha

    def fit(self, x, y):
        """
        Fit the features and the labels
        Calculate prior and feature probabilities

        Parameters
        ----------
        x: np.ndarray
            An m * n matrix - m is count of docs and n is embedding size

        y: np.ndarray
            The real class label for each doc

        Returns
        -------
        self
            Returns self as a classifier
        """
        pass

    def predict(self, x):
        """
        Parameters
        ----------
        x: np.ndarray
            An k * n matrix - k is count of docs and n is embedding size
        Returns
        -------
        np.ndarray
            Return the predicted class for each doc
            with the highest probability (argmax)
        """
        pass

    def prediction_report(self, x, y):
        """
        Parameters
        ----------
        x: np.ndarray
            An k * n matrix - k is count of docs and n is embedding size
        y: np.ndarray
            The real class label for each doc
        Returns
        -------
        str
            Return the classification report
        """
        pass

    def get_percent_of_positive_reviews(self, sentences):
        """
        You have to override this method because we are using a different embedding method in this class.
        """
        pass


# F1 Accuracy : 85%
if __name__ == '__main__':
    """
    First, find the embeddings of the revies using the CountVectorizer, then fit the model with the training data.
    Finally, predict the test data and print the classification report
    You can use scikit-learn's CountVectorizer to find the embeddings.
    """

