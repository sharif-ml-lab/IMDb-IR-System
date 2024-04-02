from .indexes_enum import Indexes, Index_types
from .index_reader import Index_reader
import json


class Tiered_index:
    def __init__(self, path="index/"):
        """
        Initializes the Tiered_index.

        Parameters
        ----------
        path : str
            The path to the indexes.
        """

        self.index = {
            Indexes.STARS: Index_reader(path, index_name=Indexes.STARS).index,
            Indexes.GENRES: Index_reader(path, index_name=Indexes.GENRES).index,
            Indexes.SUMMARIES: Index_reader(path, index_name=Indexes.SUMMARIES).index,
        }
        # feel free to change the thresholds
        self.tiered_index = {
            Indexes.STARS: self.convert_to_tiered_index(3, 2, Indexes.STARS),
            Indexes.SUMMARIES: self.convert_to_tiered_index(10, 5, Indexes.SUMMARIES),
            Indexes.GENRES: self.convert_to_tiered_index(1, 0, Indexes.GENRES)
        }
        self.store_tiered_index(path, Indexes.STARS)
        self.store_tiered_index(path, Indexes.SUMMARIES)
        self.store_tiered_index(path, Indexes.GENRES)

    def convert_to_tiered_index(
        self, first_tier_threshold: int, second_tier_threshold: int, index_name
    ):
        """
        Convert the current index to a tiered index.

        Parameters
        ----------
        first_tier_threshold : int
            The threshold for the first tier
        second_tier_threshold : int
            The threshold for the second tier
        index_name : Indexes
            The name of the index to read.

        Returns
        -------
        dict
            The tiered index with structure of 
            {
                "first_tier": dict,
                "second_tier": dict,
                "third_tier": dict
            }
        """
        if index_name not in self.index:
            raise ValueError("Invalid index type")

        current_index = self.index[index_name]
        first_tier = {}
        second_tier = {}
        third_tier = {}
        #TODO
        return {
            "first_tier": first_tier,
            "second_tier": second_tier,
            "third_tier": third_tier,
        }

    def store_tiered_index(self, path, index_name):
        """
        Stores the tiered index to a file.
        """
        path = path + index_name.value + "_" + Index_types.TIERED.value + "_index.json"
        with open(path, "w") as file:
            json.dump(self.tiered_index[index_name], file, indent=4)


if __name__ == "__main__":
    tiered = Tiered_index(
        path="index/"
    )
