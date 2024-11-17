from Jotter_ai.config.configuration import ConfigurationManager
from Jotter_ai.components.model_trainer import ModelTrainer
from Jotter_ai.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()