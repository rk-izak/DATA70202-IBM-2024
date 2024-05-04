# DATA70202 Applying Data Sciene: Working Futures 2024 Modelling and Analysis

## Dependencies
Follow the process found in the main repo's `README.md`.

Core Dependencies Include:
- Python 3.6.9
- scikit-learn==0.24.2
- xgboost==1.5.2
- lightgbm==4.3.0
- pandas==1.1.5
- numpy==1.19.5
- matplotlib==3.3.4

Other libraries can be found in `requirements.txt` file.

## File Structure
- `README.md`: Overview of the folder and its contents.
- `requirements.txt`: Required Python dependencies.
- `wf-regions-ml-2.ipynb`: Notebook for data loading, preprocessing, modelling, evaluating, and forecasting.
- `./models/lag_3`: Models' checkpoints trained using 3-year lag in the Labour Market. KNN is missing due to size restrictions.
- `./data/clean/working-futures-2024`: Data taken from the UK Government website regarding WF2024. Split into country regions and specific subregions in `.csv` file format. Relevant information can be found in `ind_info.txt` and `other_info.txt` files.

## Notebook Information and Usage

#### 1. Introduction
This Jupyter notebook is designed for machine learning model development focused on labour workforce predictions for UK regions. It covers the full pipeline from data loading and preprocessing to model training, evaluation, and predictions. 

#### 2. Notebook Structure
- **Core Imports:** Importing necessary libraries and setting up the environment.
- **Data Loading + Preprocessing:** Mechanisms for loading and preprocessing the data for model readiness.
- **Feature Engineering:** Discusses the removal of ineffective features and the refinement of the feature set.
- **Model Searching using CV:** Utilizing cross-validation to find the best machine learning models.
- **Retraining on New Features:** Retraining models with newly engineered features.
- **Models Predictions:** Generating predictions using the trained models.
- **Models Evaluations:** Assessing model performance with appropriate metrics.
- **GUI for Forecasting:** Implementation of a graphical user interface to facilitate the use of the models for forecasting.

#### 3. Setup Instructions
To run this notebook, follow these steps:
- Ensure Python 3.6.9 is installed along with the Jupyter notebook environment.
- Install required libraries mentioned in the `requirements.txt` file using pip or conda.

#### 4. Usage
- Execute the notebook cells in sequence to avoid runtime errors or missing dependencies.
- Modify the "Feature Engineering" and "Model Searching using CV" sections based on new data characteristics or desired models.
- Model training and evaluation might be timely, so please attached model checkpoints instead.
- For the GUI, pick relevant subfeatures for the market section you are interested in.

#### 5. Contributing
Contributions to the notebook are welcome. Please ensure to maintain the existing structure for consistency and readability. For more information, please refer to the author found below.

### Author: - Radoslaw Izak (radoslaw.izak@postgrad.manchester.ac.uk)
