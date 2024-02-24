import time

class Indexing:

    def __init__(self):
        # Create a class

        """
        Create a class for indexing.
        """
        return

    def indexing(self, documents):
        # The main function of the class.

        """
        Index the documents.

        Parameters
        ----------
        documents : list
            The list of documents to be indexed.

        Returns
        ----------
        dict
            The index of the documents.
        """
        return

    def construct_positional_indexes(self, corpus: str):
        """
        Get processed data and insert words in that into a trie and construct postional_index and posting lists afterwards.
        Parameters
        ----------
        corpus: str
            processed data 
        
        Return
        ----------
        docs: 
            list of docs with specified id, name,
        """
        return

    def get_posting_list(self, word: str):
        """
        get posting_list of a word
        
        Parameters
        ----------
        word: str
            word we want to check

        Return
        ----------
        dict
            posting list
        """
        return

    def store_index(self, path: str):
        """
        Stores the index in a file

        Parameters
        ----------
        path : str
            Path to store the file

        """

        return

    def load_index(self, path: str):
        """Loads the index from a file

        Parameters
        ----------
        path : str
            Path to load the file

        """

        return

    def check_if_indexing_is_good(self, documents):
        """
        Checks if the indexing is good. Do not change this function. You can use this
        function to check if your indexing is correct.

        Parameters
        ----------
        documents : list
            The list of documents which crawled

        Returns
        ----------
        bool
            True if indexing is good, False otherwise
        """

        # brute force check for "emotionally"
        start = time.time()
        check_word = "emotionally"
        docs = []
        for document in documents:
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
        posting_list = self.get_posting_list(check_word)

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

