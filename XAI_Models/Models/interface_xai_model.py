from typing import Any, List


class InterfaceXaiModel:
    def __init__(self, save_result: bool) -> None:
        pass

    def train_model(self, model: Any, data: dict, names: dict, file_name: str, chosen_sample: List[float], target_sample: float) -> str:
        """
        Trains an xai model on the ai model and returns the result.

        Parameters
        ----------
        model
            The trained ai model to analyse.
        data
            The splitted data into train and test sets.
        names
            The feature and target names.
        file_name
            The file name to save it as.
        chosen_sample
            The chosen sample to analyse.
        target_sample
            The target/true value of the chosen sample.

        Returns
        -------
        str
            A string containing the results of the xai run.
        """
        pass
