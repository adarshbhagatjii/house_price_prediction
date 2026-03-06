# 🏠 House Price Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-link.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Scikit-Learn](https://img.shields.io/badge/Library-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A full-stack Machine Learning web application that predicts real estate prices based on location, square footage, and property size. This project demonstrates a complete end-to-end pipeline—from raw data cleaning and outlier detection to a deployed interactive interface.

---

## 📌 Project Overview
The goal of this project is to provide accurate house price estimates by analyzing historical real estate data. The system handles raw data inconsistencies, performs rigorous outlier removal, and utilizes a tuned **Random Forest Regressor** to deliver predictions through a user-friendly dashboard.



## 🚀 Features
* **Data Cleaning & Engineering:** Robust handling of missing values and string-to-numeric conversions.
* **Outlier Removal:** Specialized logic to remove anomalies based on price per sqft and bed-to-bath ratios.
* **Optimized ML Model:** Hyperparameter tuning using `GridSearchCV`.
* **Interactive UI:** A user-friendly Streamlit dashboard for instant price estimation.
* **Model Persistence:** Efficient model saving and loading using `Joblib`.

## ⚙️ Tech Stack
* **Language:** Python 3.11.7
* **ML Framework:** Scikit-Learn
* **Web App:** Streamlit
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Seaborn
* **Serialization:** Joblib

---

## 📂 Project Structure
```text
house-price-prediction
│
│── house_data.csv            # Raw dataset
│── cleaned_df.csv            # Processed dataset for the app
│── rf_model.joblib           # Serialized Random Forest model
├── model_training.py             # Data pipeline & model training script
├── app.py                        # Streamlit application logic
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```






## 🧹 Data Preprocessing & Engineering

- The dataset undergoes a meticulous cleaning process to ensure model reliability:

- **Missing Value Imputation:**

- Locations filled with "Sarjapur Road".

- Size defaults to "2 BHK".

- Bathrooms filled using median values.

- **Feature Engineering:**

- Extracted numeric BHK from text descriptions.

- Converted range-based total_sqft values (e.g., "1000-1200") to their mean.

- Generated price_per_sqft for outlier detection.

- **Dimensionality Reduction:**

- Locations with $< 10$ data points are categorized as "others" to prevent overfitting.

- **Outlier Removal:**

- Removed entries where square footage per BHK was below a specific threshold.

- Filtered out properties where the number of bathrooms significantly exceeded the number of bedrooms.

- Applied Interquartile Range (IQR) filtering.

## 🤖 Machine Learning Model

- Random Forest Regressor

- We utilized a Random Forest model due to its ability to handle non-linear relationships and reduce variance.

- Hyperparameter Tuning:
- Using GridSearchCV, the following parameters were explored:

- n_estimators: [100, 150, 200, 250, 300]

- max_depth: [3, 4, 5, 6, 7]

- Evaluation Metrics:
- The model is evaluated based on:

- $R^2$ Score (Coefficient of Determination)

- Mean Absolute Error (MAE)

- Mean Squared Error (MSE)

## 🖥️ Installation & Usage

1. Clone the Repository

- git clone [https://github.com/yourusername/house-price-prediction.git](https://github.com/yourusername/house-price-prediction.git)
cd house-price-prediction


2. Install Dependencies

- pip install pandas numpy scikit-learn matplotlib seaborn streamlit joblib


3. Train the Model (Optional)

- If you wish to re-generate the rf_model.joblib file:

- python model_training.py


4. Run the Streamlit App

- streamlit run app.py


## 📊 Example Prediction

- Input Feature

- Value

- Location

- Whitefield

- Square Footage

- 1200

- BHK

- 2

- Bathrooms

- 2

- Output:

- Predicted Price: ₹75,00,000

## 📈 Future Improvements

[1] Implement One-Hot Encoding comparison with Label Encoding.

[2] Integrate XGBoost or CatBoost models for performance benchmarking.

[3] Deploy the application to Streamlit Cloud or AWS.

[4] Add interactive data distribution charts in the dashboard.

## 👨‍💻 Author

- *Adarsh Bhagat*
- *ML Engineer & Data Analyst*

- Skills: Python, Machine Learning, Streamlit, SQL, Web Dev.

- Connect: GitHub | LinkedIn

- If you find this project helpful, please consider giving it a ⭐!
