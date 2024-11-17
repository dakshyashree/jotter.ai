from Jotter_ai.config.configuration import ConfigurationManager
from Jotter_ai.components.data_transformation import DataTransformation
from Jotter_ai.logging import logger


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()