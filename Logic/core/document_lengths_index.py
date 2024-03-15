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
            Indexes.STARS.value: self.get_document_lengths(Indexes.STARS.value),
            Indexes.GENRES.value: self.get_document_lengths(Indexes.GENRES.value),
            Indexes.SUMMARIES.value: self.get_document_lengths(Indexes.SUMMARIES.value)
        }

    def get_document_lengths(self, where):
        """
        Returns the length of a document in a specific index.


        """

        # TODO: Implement this method
        return current_index


# TODO: Run the class and report 2 documents with their lengths from each index
