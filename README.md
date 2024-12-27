# KAIM Weak 3 Challenges Task 1

## AlphaCare Insurance Solutions (ACIS) Marketing Analytics Repository

Welcome to the AlphaCare Insurance Solutions (ACIS) Marketing Analytics Repository! This repository contains the code, data, models, and analysis related to our project aimed at optimizing marketing strategies and identifying low-risk targets for potential premium reductions in the South African car insurance market.

## Project Overview

Our primary objective is to leverage historical insurance claim data to perform predictive and risk analytics. By employing statistical modeling, machine learning, and hypothesis testing, we aim to:

- Identify low-risk customer segments for premium optimization.
- Explore geographic and demographic trends.
- Optimize marketing strategies by understanding feature impacts on customer behavior.

This repository is divided into four key branches, each representing a distinct task. Below is an outline of the different branches, tasks, methodologies, and tools used.

## Branch Overview

### 1. `task-1` - Exploratory Data Analysis (EDA)

**Objective**: Conduct thorough exploratory data analysis to understand the distribution and relationships within the data, detect outliers, and identify trends across different regions and customer groups.

**Key Tasks**:
- **Data Summarization**: Descriptive statistics for numerical features such as `TotalPremium`, `TotalClaim`, etc.
- **Data Structure**: Review column formats and check for missing values.
- **Univariate & Bivariate Analysis**: Analyze variable distributions and relationships using visualizations such as histograms, bar charts, scatter plots, and correlation matrices.
- **Geographic Trend Comparison**: Analyze trends by geography, such as premium types and vehicle makes across regions.
- **Outlier Detection**: Use box plots to identify outliers in numerical data.
- **Visualization**: Create three insightful visualizations to highlight key findings.

## Project Structure Overview

```bash

|   .dvcignore
|   .gitignore
|   dvc.lock
|   dvc.yaml
|   files.txt
|   folder-structure.txt
|   README.md
|   requirements
|   requirements.txt
|   
+---.dvc
|   |   .gitignore
|   |   config
  
|   +---.vscode
|   |       settings
|   |       
|   +---notebooks
|   |       eda_notebook.ipynb
|   |       __init__.py
|   |       
|   +---scripts
|   |       data_processing.py
|   |       data_visualization.py
|   |       load_data.py
|   |       __init__.py
|   |       
|   +---src
|   |       __init__.py
|   |       
|   \---tests
|           __init__.py
|           
+---Data
|   |   .gitignore
|   |   raw.dvc
|   |   
|   +---interim
|   |       .gitignore
|   |       MachineLearningRating_v3.txt
|   |       
|   +---processed
|   |       cleaned_data.csv
|   |       
|   +---raw
|   |       MachineLearningRating_v3.zip
|   |       
|   \---visualizations
|           correlation_heatmap.png
|           geographical_trends.png
|           outliers_boxplot.png
|           premium_by_cover.png
|           
+---notebooks
|       eda_notebook.ipynb
|       __init__.py
|       
+---scripts
|   |   data_processing.py
|   |   data_visualization.py
|   |   load_data.py
|   |   __init__.py
|   |   
|   \---__pycache__
|           data_processing.cpython-312.pyc
|           data_visualization.cpython-312.pyc
|           load_data.cpython-312.pyc
|           
+---src
|       __init__.py
|       
\---tests
        test_data_processing.py
        __init__.py
        


```


## How to Get Started

### Prerequisites

- Python 3.8+
- Libraries: `pandas`, `numpy`, `matplotlib`, `scikit-learn`, `xgboost`, `dvc`, `shap`, `lime`, `seaborn`, etc.
- Jupyter Notebook for running the analysis.
- DVC for data version control.

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Jenber-Ligab/ACIS
   cd KAIM-W3
   git checkout task-1
   ```

2. **Install Dependencies**
3. **Run Notebooks**

## Key Insights and Recommendations

- **Risk Analysis**: Early insights suggest significant risk differences between provinces and gender groups, which could be used to tailor marketing strategies and adjust premiums.
- **Geographic Trends**: Zipcode-level analysis shows disparities in claim rates and insurance types, suggesting location-based pricing strategies.
- **Predictive Modeling**: Random Forest and XGBoost models showed strong predictive power for total claims, with features such as car age and geographic location being the most important predictors.

## Conclusion

This project provides actionable insights to optimize marketing strategies, improve customer segmentation, and enhance premium pricing models for AlphaCare Insurance Solutions. By leveraging data analytics, statistical testing, and machine learning, we aim to drive business growth and customer satisfaction.

Thank you for using this repository! For any issues or contributions, please feel free to submit a pull request or contact the project maintainers.
