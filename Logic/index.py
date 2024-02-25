import time

class Index:
    def __init__(self, preprocessed_documents: list):
        """
        Create a class for indexing.
        """

        self.preprocessed_documents = preprocessed_documents

    def index_stars(self):
        """
        Index the documents based on the stars.

        Returns
        ----------
        dict
            The index of the documents based on the stars.
        """
        return

    def index_genres(self):
        """
        Index the documents based on the genres.

        Returns
        ----------
        dict
            The index of the documents based on the genres.
        """
        return

    def index_summaries(self):
        """
        Index the documents based on the summaries (not first_page_summary).

        Returns
        ----------
        dict
            The index of the documents based on the summaries.
        """
        return

    def index_reviews(self):
        """
        Index the documents based on the reviews.

        Returns
        ----------
        dict
            The index of the documents based on the reviews.
        """
        return

    def get_posting_list(self, word: str, index_type: str):
        """
        get posting_list of a word
        
        Parameters
        ----------
        word: str
            word we want to check
        index_type: str
            type of index we want to check (stars, genres, summaries, reviews)

        Return
        ----------
        dict
            posting list
        """
        return

    def add_document_to_index(self, document: dict):
        """
        Add a document to all the indexes

        Parameters
        ----------
        document : dict
            Document to add to all the indexes

        """

        pass

    def remove_document_from_index(self, document_id: int):
        """
        Remove a document from all the indexes

        Parameters
        ----------
        document_id : int
            ID of the document to remove from all the indexes

        """

        pass

    def store_index(self, path: str, index_type: str):
        """
        Stores the index in a file (such as a JSON file)

        Parameters
        ----------
        path : str
            Path to store the file
        index_type: str
            type of index we want to store (stars, genres, summaries, reviews)

        """

        pass

    def load_index(self, path: str):
        """
        Loads the index from a file (such as a JSON file)

        Parameters
        ----------
        path : str
            Path to load the file

        """

        pass

    def check_if_indexing_is_good(self, index_type, check_word="emotionally"):
        """
        Checks if the indexing is good. Do not change this function. You can use this
        function to check if your indexing is correct.

        Parameters
        ----------
        index_type : str
            Type of index to check (stars, genres, summaries, reviews)
        check_word : str
            The word to check in the index

        Returns
        ----------
        bool
            True if indexing is good, False otherwise
        """

        # brute force to check check_word in the summaries
        start = time.time()
        docs = []
        for document in self.preprocessed_documents:
            for summary in document['summaries']:
                if check_word in summary:
                    docs.append(document['id'])

                    # if we have found 3 documents with the word, we can break
                    if len(docs) == 3:
                        break

        end = time.time()
        brute_force_time = end - start


        # check by getting the posting list of the word
        start = time.time()
        # based on your implementation, you may need to change the following line
        posting_list = self.get_posting_list(check_word, index_type)

        end = time.time()
        implemented_time = end - start


        print("Brute force time: ", brute_force_time)
        print("Implemented time: ", implemented_time)

        if set(docs).issubset(set(posting_list)):
            print("Indexing is correct")

            if implemented_time < brute_force_time:
                print("Indexing is good")
                return True
            else:
                print("Indexing is bad")
                return False
        else:
            print("Indexing is wrong")
            return False

