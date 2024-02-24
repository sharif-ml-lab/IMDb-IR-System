

class Preprocessor:

    def __init__(self, stopwords_path):
        # Create a variable of stop words.
        self.stopwords = []

    def preprocess(self, text):
        # The main function of the class.

        """
        Preprocess the text.

        Parameters
        ----------
        text : str
            The text to be preprocessed.

        Returns
        ----------
        str
            The preprocessed text.
        """
        return

    def normalize(self, text):
        # Normalize text (lower case, stemming, lemmatization, etc.)

        """
        Normalize the text.

        Parameters
        ----------
        text : str
            The text to be normalized.

        Returns
        ----------
        str
            The normalized text.
        """
        return

    def remove_links(self, text):
        # Remove links

        """
        Remove links from the text.

        Parameters
        ----------
        text : str
            The text to be processed.

        Returns
        ----------
        str
            The text with links removed.
        """
        return

    def remove_punctuations(self, text):
        # Remove punctuations

        """
        Remove punctuations from the text.

        Parameters
        ----------
        text : str
            The text to be processed.

        Returns
        ----------
        str
            The text with punctuations removed.
        """
        return

    def word_tokenize(self, word):
        # Tokenize text

        """
        Tokenize the words in the text.

        Parameters
        ----------
        word : str
            The word to be tokenized.

        Returns
        ----------
        list
            The list of words.
        """
        return

    def remove_stopwords(self, words):
        # Remove stopwords

        """
        Remove stopwords from the text.

        Parameters
        ----------
        words : list
            The list of words to be processed.

        Returns
        ----------
        list
            The list of words with stopwords removed.
        """
        return

