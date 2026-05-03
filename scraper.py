import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

URL = "https://example.com/product"  # replace

def fetch_price():
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(URL, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # ⚠️ Update class based on site
    price = soup.find("span", {"class": "price"}).text.strip()

    return price

def save_price(price):
    with open("price_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), price])

if __name__ == "__main__":
    p = fetch_price()
    print("Price:", p)
    save_price(p)
