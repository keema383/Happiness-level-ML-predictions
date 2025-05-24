> Predicting Happiness from Survey Data using Machine Learning. Includes data cleaning, feature engineering, and classification models (KNN, Decision Tree) applied to national self-reported well-being data.

# README: Happiness Prediction Using Survey Data

## Project Overview
This project explores the prediction of self-reported happiness levels based on socio-economic, health, political, and attitudinal variables collected through a national survey. The target variable, `RATEHAP`, was cleaned, mapped, and modeled using multiple machine learning algorithms.

## Dataset
- **Source**: [Caucasus Barometer 2024 (Armenia)](https://caucasusbarometer.org/en/cb2024am/codebook/)
- **Access Method**: The `.dta` file was downloaded from the official CRRC Caucasus Barometer site and transformed into a `.csv` format using Python.
- **Size**: ~1,500 respondents
- **Target Variable**: `RATEHAP` (Happiness level)
- **Features**: Demographics, health, trust, religiosity, media use, political views, etc.

## Preprocessing
- Removed identifiers and irrelevant weights.
- Cleaned target and feature variables by mapping qualitative responses (Likert scales, yes/no, etc.) to numeric values.
- Dropped or imputed rows with missing values.
- Applied one-hot encoding to categorical features.
- Scaled features using `StandardScaler` for models sensitive to feature magnitude (e.g., KNN).

## Feature Engineering
- Custom function `replace_survey_words()` was developed to handle over 50 unique text-to-numeric mappings.
- Random Forest used to extract feature importances.
- Top 40 most predictive features were selected for final model training.
- Cleaned and transformed datasets are saved in the `Data/` folder as `.csv` and Excel files.

## Models Used
- **K-Nearest Neighbors (KNN)**
  - Optimal K determined using elbow method (k=9)
  - Test Accuracy: **70.59%**

- **Decision Tree Classifier**
  - Test Accuracy: **58.82%**

- **Logistic Regression**
  - Considered but excluded due to unmet assumptions (linearity, multicollinearity).

## Target Categorization
- RATEHAP converted into 3 classes:
  - Low Happiness: <3
  - Mid Happiness: 3–5
  - High Happiness: >=6

## File Structure
- `Happiness_Prediction_Model.ipynb`: Full modeling pipeline (cleaning, feature engineering, training, evaluation)
- `Data/clean_data.xlsx`: Cleaned final dataset
- `Data/Data_Cleaning.ipynb`: Cleaning and preprocessing logic
- `Data/transform to CSV.py`: Script used to convert `.dta` file to `.csv`
- `README.md`: Project description and usage guide

## How to Run
1. Open `Happiness_Prediction_Model.ipynb` in Jupyter Notebook.
2. Run all cells to reproduce data preprocessing, modeling, and evaluation.

## Requirements
- Python 3.7+
- pandas, numpy, matplotlib, scikit-learn

## Authors
- Kima Badalyan — American University of Armenia
- Armine Hakobyan — American University of Armenia
- Nare Sargsyan — American University of Armenia
- Ruben Galoyan — American University of Armenia

## License
This project is for academic use only.
