# BTC-Price-Preditction
Bitcoin Price Movement Predictor
This project uses machine learning to predict whether the price of Bitcoin (BTC-USD) will go up or down the next day, based on historical price data. It applies basic feature engineering and trains a Random Forest Classifier to make binary predictions.

Overview
Fetches the last 90 days of Bitcoin data using the Yahoo Finance API (yfinance)


Engineers features like:


Daily percentage return


5-day moving average (MA5)


10-day moving average (MA10)


Trains a Random Forest Classifier using these features


Evaluates model performance using accuracy and classification metrics


Predicts the next day's movement: 📈 "UP" or 📉 "DOWN"


Visualizes Bitcoin's closing price over the last 90 days using matplotlib



How It Works
Data Collection: Pulls BTC-USD data from the last 90 days


Feature Engineering: Calculates:


Daily returns


Moving averages


Labels indicating whether the next day's price increased


Model Training: Random Forest Classifier is trained on historical data


Prediction: Makes a prediction based on the most recent features


Visualization: Plots BTC price trend using a line graph


Getting Started
1. Clone the repository:
git clone https://github.com/yourusername/btc-price-predictor.git
cd btc-price-predictor

2. Install dependencies:
pip install -r requirements.txt


3. Run the script:
python btc_predictor.py

Technologies Used
Python 


yfinance – to fetch Bitcoin price data


pandas, numpy – for data manipulation


scikit-learn – for machine learning model


matplotlib – for plotting BTC price trend


Project Status
Functional prototype — predicts next-day BTC price direction using a basic Random Forest model.
 Future improvements: Add more indicators (RSI, MACD), hyperparameter tuning, and backtesting strategy.

