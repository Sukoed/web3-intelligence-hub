import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']
        print(f"Current Bitcoin Price: ${price}")
    except Exception as e:
        print(f"Error fetching price: {e}")

if __name__ == "__main__":
    get_btc_price()
