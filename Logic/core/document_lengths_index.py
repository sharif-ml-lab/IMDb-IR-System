import json
from indexes_enum import Indexes


class DocumentLengthsIndex:
    def __init__(self, documents_index):
        """
        Initializes the DocumentLengthsIndex.

        Parameters
        ----------
        documents_index : dict
            A dictionary of indexes for the documents.
        """

        self.documents_index = documents_index
        self.document_length_index = {
            Indexes.STARS.value: self.get_documents_length(Indexes.STARS.value),
            Indexes.GENRES.value: self.get_documents_length(Indexes.GENRES.value),
            Indexes.SUMMARIES.value: self.get_documents_length(Indexes.SUMMARIES.value)
        }

    def get_documents_length(self, where):
        """
        Gets the documents' length for the specified field.

        Parameters
        ----------
        where : str
            The field to get the document lengths for.

        Returns
        -------
        dict
            A dictionary of the document lengths. The keys are the document IDs, and the values are
            the document's length in that field (where).
        """

        # TODO: Implement this method
        return current_index


# TODO: Run the class and report 2 documents with their lengths from each index
