#imports
#Imports pipeline classes for each stage from the Jotter_ai.pipeline module.
#Imports a logger for logging messages, errors, and progress updates.
from Jotter_ai.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Jotter_ai.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Jotter_ai.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Jotter_ai.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from Jotter_ai.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from Jotter_ai.logging import logger

#Purpose: Collect and prepare raw data for the pipeline.
#The DataIngestionTrainingPipeline class likely performs tasks like:
#Downloading data.
#Splitting data into train/test sets.
#Storing data in a structured format.
#Flow:
#Logs the start of the stage.
#Executes the main() method of DataIngestionTrainingPipeline.
#Logs the successful completion or an exception if it occurs.
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



#Purpose: Validate the ingested data for quality and consistency.
#Likely performs tasks like:
#Checking for missing values.
#Validating data schema or formats.
#Removing invalid or duplicate records.
#Flow:
#Similar to the data ingestion stage.
STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


#Purpose: Prepare the data for training.
#Likely includes:
#Feature engineering (e.g., normalization, scaling, or encoding categorical variables).
#Creating new derived features.
#Storing the transformed data for the next stage.
#Flow:
#Logs the start and completion of the stage.
STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


#Purpose: Train the machine learning model.
#Likely involves:
#Initializing a model.
#Training it on the transformed data.
#Storing the trained model for evaluation.
#Flow:
#Logs progress and any exceptions during training.
STAGE_NAME = "Model Trainer stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_trainer = ModelTrainerTrainingPipeline()
   model_trainer.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



#Purpose: Evaluate the trained model's performance.
#Likely includes:
#Measuring metrics like accuracy, precision, recall, F1-score, etc.
#Comparing results to baseline models or benchmarks.
#Generating evaluation reports or visualizations.
#Flow:
#Similar to previous stages, with logging and exception handling.
STAGE_NAME = "Model Evaluation stage"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   model_evaluation = ModelEvaluationTrainingPipeline()
   model_evaluation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e




