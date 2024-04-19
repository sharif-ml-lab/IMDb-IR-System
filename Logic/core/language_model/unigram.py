from math import log2
import seaborn
import matplotlib.pyplot as plt
import nltk
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from .tokenizer import Tokenizer

nltk.download("punkt")


def set_style(plt):
    plt.style.use("seaborn-v0_8")
    plt.rcParams["legend.numpoints"] = 1
    plt.rcParams["axes.labelsize"] = 20
    plt.rcParams["axes.titlesize"] = 20
    plt.rcParams["xtick.labelsize"] = 15
    plt.rcParams["ytick.labelsize"] = 15
    plt.rcParams["legend.fontsize"] = 10
    return plt


legend_opts = {
    "fontsize": 15,
    "frameon": True,
    "framealpha": 1,
    "facecolor": "white",
    "edgecolor": "black",
    "labelspacing": 0.1,
}


def savefig(fig, filenaشme, **kwargs):
    fig.savefig(f"../viz/{filename}", bbox_inches="tight", **kwargs)


# plt = set_style(plt)


class UnigramCounter:
    def __init__(self, file_name: str, tokenizer: Tokenizer) -> None:
        """
        Initialize unigram counter from tokenized text and count number of unigrams in text

        Paramters
        ---------
        file_name: str
            Path of tokenized text. Each line is a sentence with tokens separated by comma
        tokenizer: Tokenizer
            Tokenizer is used to tokenize text
        """
        self.sentence_generator = tokenizer.get_tokenized_sentences(file_name)
        self.count()

    def count(self) -> None:
        """
        Count number of unigrams in text, one sentence at a time
        """
        # TODO


class UnigramModel:
    def __init__(self, train_counter: UnigramCounter) -> None:
        """
        Initialize unigram model from unigram counter, count the number of unique unigrams (vocab)

        Paramters
        ---------
        train_counter: UnigramCounter
            counted unigram counter
        """
        self.counter = train_counter
        self.counts = train_counter.counts.copy()
        self.counts["[UNK]"] = 0
        self.vocab = set(self.counts.keys())
        self.vocab_size = len(self.vocab)

    def train(self, k: int = 1) -> None:
        """
        For each unigram in the vocab, calculate its probability in the text

        Paramters
        ---------
        k: int
            smoothing pseudo-count for each unigram
        """
        # TODO

    def evaluate(self, evaluation_counter: UnigramCounter) -> float:
        """
        Calculate the average log likelihood of the model on the evaluation text

        Paramters
        ---------
        evaluation_counter: UnigramCounter
            unigram counter for the text on which the model is evaluated on

        Returns
        ---------
        float
            average log likelihood that the unigram model assigns to the evaluation text
        """
        # TODO


if __name__ == "__main__":
    # TODO: You should do these steps:
    # 1. Load the dataset (e.g. using pd.read_csv)
    # 2. Tokenize the dataset properly (using your Tokenizer class)
    # 3. Create `UnigramCounter` and `UnigramModel` for your data
    # 4. Create model and train
    # 5. Plot the results of your code. show the most and least commnon words.
    # 6. show the words ditstrubution.
    # 7. show each result with or without smoothing
    # IMPORTANT NOTE: for plotting, you should use Wandb (You will need this for the next parts and phases, too!)
    pass
