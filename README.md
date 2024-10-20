# Customer Churn Prediction

## Overview
This project focuses on predicting customer churn using machine learning techniques. The goal is to identify customers who are likely to stop using a company's services, enabling businesses to take proactive measures to retain them.

A **Support Vector Machine(SVM)** classifier was used to build the model, which was then deployed using a **Flask** web application with API endpoints for real-time predictions.

## Project Structure
- **Exploratory Data Analysis (EDA)**: Analysis to identify key features that affect customer churn.
- **Model Building**: To improve model performance, multiple approaches, including undersampling, oversampling using SMOTE and hyperparameter tuning, were tried.
- **Deployment**: The final model was deployed using Flask with a functional API.

## Key Features
- **Model**: Random Forest Classifier
- **Performance**: 
  - Accuracy: **87%**
  - Recall: **49%** 
 
- **Model**: Decision Tree (After undersampling)
- **Performance**: 
  - Accuracy: **82%**
  - Recall: **60%**
    
  **Model**: Support Vector Machine  (After SMOTE)
- **Performance**: 
  - Accuracy: **84%**
  - Recall: **68%**
    
  
- **Deployment**: Flask app with API endpoints, tested with Postman.
  
## Methods Used
- **Data Preprocessing**: Handled missing values, removed outliers, and scaled features using StandardScaler.
- **Feature Engineering**: Experimented with new features but avoided methods that reduced model performance.
- **Undersampling**: Applied to improve model balance and recall.
- **SMOTE**: Applied to improve the recall and solve the class imbalance problem.

## Getting Started

### Requirements
- Python 3.x
- Libraries:
  - Flask
  - Scikit-learn
  - Pandas
  - Numpy
  - Postman (for testing API)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jayjoshi33/customer-churn-prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask app:
   ```bash
   python app.py
   ```
4. Use Postman or a similar tool to test the API by sending JSON input for predictions.

## API Usage
- **Endpoint**: `/predict`
- **Method**: POST
- **Input**: Customer data in JSON format.
- **Output**: Predicted class (churn or not churn).

## Results
- The Random Forest model achieved **87% accuracy** with **49% recall**.
- After applying SMOTE, a SVC model improved recall to **68%**.

## Conclusion
This project provides a predictive model for customer churn, allowing businesses to identify potential churners and take necessary actions. The model is deployed via Flask, with easy API access for real-time predictions.
