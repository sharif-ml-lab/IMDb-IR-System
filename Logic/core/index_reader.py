from .indexes_enum import Indexes,Index_types
import json
class Index_reader:
    def __init__(self,path: str, index_name: Indexes, index_type: Index_types = None):
        """
        Initializes the Index_reader.

        Parameters
        ----------
        path : str
            The path to the indexes.
        index_name : Indexes
            The name of the index to read.
        index_type : Index_types
            The type of the index to read.  
        """
        self.path = path
        self.index_name = index_name
        self.index_type = index_type
        self.index = self.get_index()

    def get_index(self):
        """
        Gets the index from the file.

        Returns
        -------
        dict
            The index.
        """
        absolute_path = self.path + self.index_name.value
        
        if self.index_type != None:
            absolute_path = absolute_path + "_" + self.index_type.value

        absolute_path = absolute_path + "_index.json"
        
        with open(absolute_path, 'r') as file:
            return json.load(file)
        
    
        