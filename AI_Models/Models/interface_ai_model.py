from typing import Tuple


class InterfaceAiModel:
    def train_model(self, dataset_url: str) -> Tuple[any, dict, dict]:
        pass
