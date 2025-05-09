# Step 1: Import all libraries
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Step 2: Download historical BTC data
def fetch_btc_data():
    btc = yf.download('BTC-USD', period='90d', interval='1d')
    return btc

# Step 3: Feature engineering
def engineer_features(btc):
    btc['Return'] = btc['Close'].pct_change()
    btc['MA5'] = btc['Close'].rolling(window=5).mean()
    btc['MA10'] = btc['Close'].rolling(window=10).mean()
    btc['Label'] = (btc['Close'].shift(-1) > btc['Close']).astype(int)
    btc.dropna(inplace=True)
    return btc

# Step 4: Model training
def train_model(btc):
    X = btc[['Return', 'MA5', 'MA10']]
    y = btc['Label']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"\nAccuracy: {acc:.2f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    return model, X

# Step 5: Make tomorrow's prediction
def predict_tomorrow(model, X):
    latest_data = X.iloc[-1].values.reshape(1, -1)
    prediction = model.predict(latest_data)[0]
    print("\nPrediction for Tomorrow:")
    print("UP" if prediction == 1 else "DOWN")

# Step 6: Plot BTC closing price with Matplotlib
def plot_btc_price(btc):
    plt.figure(figsize=(10, 5))
    plt.plot(btc.index, btc['Close'], label='BTC Price', color='blue')
    plt.title('Bitcoin Price (Last 90 Days)')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

# Main function
def main():
    print("Bitcoin Price Prediction Model\n")
    btc_data = fetch_btc_data()
    btc_data = engineer_features(btc_data)
    model, features = train_model(btc_data)
    predict_tomorrow(model, features)
    plot_btc_price(btc_data)

# Entry point
if __name__ == "__main__":
    main()
