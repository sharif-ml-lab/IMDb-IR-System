
from typing import List

class Evaluation:

    def calculate_precision(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the precision of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The precision of the predicted results
        """
        precision = 0.0

        # TODO: Calculate precision here
        
        return precision
    
    def calculate_recall(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the recall of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The recall of the predicted results
        """
        recall = 0.0

        # TODO: Calculate recall here

        return recall
    
    def calculate_F1(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the F1 score of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The F1 score of the predicted results    
        """
        f1 = 0.0

        # TODO: Calculate F1 here

        return f1
    
    def calculate_AP(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Mean Average Precision of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The Average Precision of the predicted results
        """
        AP = 0.0

        # TODO: Calculate AP here

        return AP
    
    def calculate_MAP(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Mean Average Precision of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The Mean Average Precision of the predicted results
        """
        MAP = 0.0

        # TODO: Calculate MAP here

        return MAP
    
    def cacluate_DCG(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Normalized Discounted Cumulative Gain (NDCG) of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The DCG of the predicted results
        """
        DCG = 0.0

        # TODO: Calculate DCG here

        return DCG
    
    def cacluate_NDCG(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Normalized Discounted Cumulative Gain (NDCG) of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The NDCG of the predicted results
        """
        NDCG = 0.0

        # TODO: Calculate NDCG here

        return NDCG
    
    def cacluate_RR(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Mean Reciprocal Rank of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The Reciprocal Rank of the predicted results
        """
        RR = 0.0

        # TODO: Calculate MRR here

        return RR
    
    def cacluate_MRR(self, actual: List[List[str]], predicted: List[List[str]]) -> float:
        """
        Calculates the Mean Reciprocal Rank of the predicted results

        Parameters
        ----------
        actual : List[List[str]]
            The actual results
        predicted : List[List[str]]
            The predicted results

        Returns
        -------
        float
            The MRR of the predicted results
        """
        MRR = 0.0

        # TODO: Calculate MRR here

        return MRR
    
    def print_evaluation(self, actual: List[List[str]], predicted: List[List[str]]):
        # TODO: Call evaluation functions here and report the results
        print(f"precision = {self.calculate_precision(actual, predicted)}")
        print(f"recall = {self.calculate_recall(actual, predicted)}")
        print(f"F1 = {self.calculate_F1(actual, predicted)}")
        print(f"MAP = {self.calculate_MAP(actual, predicted)}")
        print(f"NDCG = {self.cacluate_NDCG(actual, predicted)}")
        print(f"MRR = {self.cacluate_MRR(actual, predicted)}")


