# Predictive Modeling Using Machine Learning

## Project Overview

This project demonstrates the implementation of machine learning algorithms to predict student performance based on academic scores. The objective is to build predictive models, evaluate their performance, and visualize the results using standard machine learning evaluation metrics.

The project follows the complete machine learning workflow, including data collection, preprocessing, model training, testing, evaluation, and result visualization.

---

## Objectives

* Understand the fundamentals of supervised machine learning.
* Build predictive models using classification algorithms.
* Train and test machine learning models on real-world data.
* Evaluate model performance using accuracy metrics.
* Visualize results using Confusion Matrix and ROC Curve.
* Compare the performance of different machine learning algorithms.

---

## Dataset

### Dataset Name

Student Performance Dataset

### Description

The dataset contains student academic information and examination scores. The data is used to predict whether a student passes or fails based on selected performance indicators.

### Features Used

* Reading Score
* Writing Score

### Target Variable

Result

* 1 = Pass
* 0 = Fail

The target variable was created based on the student's mathematics score:

* Pass: Mathematics Score ≥ 50
* Fail: Mathematics Score < 50

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

### Development Environment

* Visual Studio Code (VS Code)

---

## Machine Learning Algorithms Used

### 1. Decision Tree Classifier

A Decision Tree Classifier is a supervised learning algorithm that creates decision rules from the dataset and predicts outcomes based on those rules.

Advantages:

* Easy to understand
* Fast training
* Suitable for classification tasks

### 2. Random Forest Classifier

Random Forest is an ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

Advantages:

* High accuracy
* Robust performance
* Better generalization

---

## Project Workflow

### Step 1: Import Required Libraries

The necessary Python libraries were imported for data processing, visualization, model building, and evaluation.

### Step 2: Load Dataset

The dataset was loaded using Pandas and inspected to understand its structure and attributes.

### Step 3: Data Preprocessing

A new column named "Result" was created to classify students as Pass or Fail based on their mathematics score.

### Step 4: Feature Selection

The following features were selected:

* Reading Score
* Writing Score

These features were used to predict the Result variable.

### Step 5: Train-Test Split

The dataset was divided into:

* 80% Training Data
* 20% Testing Data

This ensures unbiased model evaluation.

### Step 6: Model Training

The following models were trained:

* Decision Tree Classifier
* Random Forest Classifier

### Step 7: Prediction

The trained models were used to predict student outcomes on unseen test data.

### Step 8: Model Evaluation

Model performance was evaluated using:

* Accuracy Score
* Confusion Matrix
* ROC Curve
* AUC Score

---

## Evaluation Metrics

### Accuracy Score

Measures the percentage of correct predictions made by the model.

Formula:

Accuracy = Correct Predictions / Total Predictions

### Confusion Matrix

Displays:

* True Positives
* True Negatives
* False Positives
* False Negatives

This helps understand model performance in detail.

### ROC Curve

The Receiver Operating Characteristic (ROC) Curve visualizes the model's ability to distinguish between classes.

### AUC Score

Area Under Curve (AUC) measures the overall classification performance.

Higher AUC indicates better performance.

---

## Results

### Decision Tree Classifier

* Successfully trained on the dataset.
* Generated predictions with high accuracy.

### Random Forest Classifier

* Successfully trained on the dataset.
* Achieved excellent prediction accuracy.
* Demonstrated strong classification performance.

### Visualizations Generated

* Confusion Matrix
* ROC Curve

---

## Project Structure

```text
Predictive-Modeling-Using-ML/
│
├── predictive_model.py
├── StudentsPerformance.csv
├── README.md
├── confusion_matrix.png
└── roc_curve.png
```

## Future Improvements

* Use larger datasets for improved generalization.
* Apply feature engineering techniques.
* Compare additional algorithms such as:

  * Logistic Regression
  * Support Vector Machine (SVM)
  * K-Nearest Neighbors (KNN)
  * XGBoost
* Deploy the model as a web application using Flask or Streamlit.

---

## Conclusion

This project successfully demonstrates the application of machine learning techniques for predictive modeling. Decision Tree and Random Forest algorithms were implemented to classify student performance. The models were evaluated using accuracy scores, confusion matrices, and ROC curves. The project provides practical experience in supervised learning, model evaluation, and data analysis using Python.

---

## Author

**Syeed Hasan**

Data Science Student

Machine Learning Internship Project - Thiranex
