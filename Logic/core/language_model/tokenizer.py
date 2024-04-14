from nltk.tokenize import RegexpTokenizer, sent_tokenize
from typing import Iterator

class Tokenizer:
    def __init__(self):
        pass

    def replace_characters(self, text: str) -> str:
        """
        Replace tricky punctuations that can mess up sentence tokenizers
        Paramters
        ---------
        text: str
            text with non-standard punctuations
        Returns
        ---------
        str
            text with standardized punctuations
        """
        # TODO

    def tokenize_raw_text(self, raw_text_path: str, token_text_path: str) -> None:
        """
        Read a input text file and write its content to an output text file in the form of tokenized sentences
        Paramters
        ---------
        raw_text_path: str
            path of raw input text file
        token_text_path: str
            path of tokenized output text file
        """
        # TODO

    def get_tokenized_sentences(self, file_name: str) -> Iterator[str]:
        """
        Return tokenized sentence one at a time from a tokenized text
        Paramters
        ---------
        file_name: str
            path of tokenized text
        """
        # TODO