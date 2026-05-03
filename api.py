from fastapi import FastAPI
from transform import process_data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Price Intelligence API"}

@app.get("/prices")
def get_prices():
    df = process_data()
    return df.tail(10).to_dict(orient="records")

@app.get("/buy-signal")
def get_signal():
    df = process_data()
    latest = df.iloc[-1]
    
    return {
        "current_price": latest["price"],
        "min_price": latest["min_price"],
        "buy": bool(latest["buy_signal"])
    }
