from AI_Models.interface_ai_model import InterfaceAiModel


class TestAiModel(InterfaceAiModel):
    def train_model(self, dataset_url):
        print("Finished training AI Model...")
        return 0, 0
