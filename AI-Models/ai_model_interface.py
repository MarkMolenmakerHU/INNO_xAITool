from typing import Tuple


class AiModelInterface:
    def train_model(self, dataset_url: str) -> Tuple[float, float]:
        return
