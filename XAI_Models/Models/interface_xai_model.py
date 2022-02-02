from typing import Any, Dict, List


class InterfaceXaiModel:
    def __init__(self, save_result) -> None:
        pass
    
    def train_model(self, model: Any, data: Dict, names: Dict, file_name: str, chosen_sample: List[float], target_sample: float) -> str:
        pass
