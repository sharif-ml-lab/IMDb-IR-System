import json
import numpy as np
from preprocess import Preprocessor


class SearchEngine:
    def __init__(self, documents, document_indexes, average_document_field_length):
        """
        Initializes the search engine.

        Parameters
        ----------
        documents : dict
            A dictionary of documents without any preprocessing.
        document_indexes : dict
            A dictionary of indexes for the documents.
        average_document_field_length : dict
            A dictionary of the average field lengths for the documents.
        """

        self.documents = documents
        self.document_indexes = document_indexes
        self.average_document_field_length = average_document_field_length

    def search(self, query, method, where, max_results=10):
        """
        Returns a list of documents that match the query.

        Parameters
        ----------
        query : str
            The query to search for.
        method : str ((n|l)(n|t)(n|c).(n|l)(n|t)(n|c)) | OkapiBM25
            The method to use for searching.
        where : str
            The index to search in.
        max_results : int
            The maximum number of results to return. If None, all results are returned.
        """

        if method == 'OkapiBM25':
            result = self.okapi_bm25(query, where)
        else:
            result = self.vector_space_model(query, method, where)

        # TODO: Sort the results and return the top max_results (Pay attention to max_results=None
        return result

    def get_tf(self, term, document_id, where):
        """
        Returns the term frequency of a term in a document.

        Parameters
        ----------
        term : str
            The term to get the term frequency for.
        document_id : str
            The document to get the term frequency for.
        where : str
            The index to search in.
        """

        # TODO
        return

    def get_df(self, term, where):
        """
        Returns the document frequency of a term.

        Parameters
        ----------
        term : str
            The term to get the document frequency for.
        where : str
            The index to search in.
        """

        # TODO
        return

    def get_idf(self, term, where):
        """
        Returns the inverse document frequency of a term.

        Parameters
        ----------
        term : str
            The term to get the inverse document frequency for.
        where : str
            The index to search in.
        """

        # TODO
        return

    def okapi_bm25(self, query, where):
        """
        Returns a list of documents that match the query using the Okapi BM25 method.

        Parameters
        ----------
        query : str
            The query to search for.
        where : str
            The index to search in.
        """

        # TODO
        return

    def get_okapi_bm25_score(self, query, document_id, where):
        """
        Returns the Okapi BM25 score of a document for a query.

        Parameters
        ----------
        query : str
            The query to search for.
        document_id : str
            The document to calculate the score for.
        where : str
            The index to search in.
        """

        # TODO
        return

    def get_content_length(self, content: list):
        """
        Returns the length of the content.

        Parameters
        ----------
        content : list
            The content to get the length of.
        """

        # TODO
        return

    def vector_space_model(self, query, method, where):
        """
        Returns a list of documents that match the query using the Vector Space Model method.

        Parameters
        ----------
        query : str
            The query to search for.
        method : str ((n|l)(n|t)(n|c).(n|l)(n|t)(n|c))
            The method to use for searching.
        where : str
            The index to search in.
        """

        # TODO
        return

    def get_vector_space_model_score(self, query, document_id, where, document_method, query_method):
        """
        Returns the Vector Space Model score of a document for a query.

        Parameters
        ----------
        query : str
            The query to search for.
        document_id : str
            The document to calculate the score for.
        where : str
            The index to search in.
        document_method : str (n|l)(n|t)(n|c)
            The method to use for the document.
        query_method : str (n|l)(n|t)(n|c)
            The method to use for the query.
        """

        # TODO
        return


def get_average_document_field_length(where):
    """
    Returns the sum of the field lengths of all documents in the index.

    Parameters
    ----------
    where : str
        The index to search in.
    """

    # TODO
    return

# TODO: Run the search function for two different queries and for each index (2 queries * 3 indexes = 6 results)
# TODO: Finally report the results (upload the results in Quera)
