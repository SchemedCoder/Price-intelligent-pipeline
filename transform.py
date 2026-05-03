import pandas as pd

def process_data():
    df = pd.read_csv("price_log.csv", names=["date", "price"])

    # Clean price (₹, commas)
    df["price"] = df["price"].replace('[₹,]', '', regex=True).astype(float)

    # Rolling min (14 days logic)
    df["min_price"] = df["price"].rolling(window=14, min_periods=1).min()

    # Buy signal
    df["buy_signal"] = df["price"] <= df["min_price"]

    return df

if __name__ == "__main__":
    df = process_data()
    print(df.tail())
