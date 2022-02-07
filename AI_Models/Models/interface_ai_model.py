from typing import Tuple


class InterfaceAiModel:
    def train_model(self, dataset: dict) -> Tuple[any, dict, dict]:
        """
        Trains an ai model on the dataset and returns it.

        Parameters
        ----------
        dataset
            A dictionary containing the data and all the details about it.

        Returns
        -------
        tuple
            A tuple containing the trained model, the splitted data and the scores.
        """
        pass
