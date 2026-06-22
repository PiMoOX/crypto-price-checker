import requests

def get_crypto_price():
    """Fetch live prices of top 100 cryptocurrencies from CoinLore API"""
    api_url = "https://api.coinlore.net/api/tickers/"
    response = requests.get(api_url)
    data = response.json()

    coins = data["data"]
    crypto_name = input("Enter crypto name or symbol: ")

    for coin in coins[:100]:
        if crypto_name.lower() == coin["name"].lower() or crypto_name.lower() == coin["symbol"].lower():
            print(f"Name: {coin['name']} ({coin['symbol']})")
            print(f"Price: ${coin['price_usd']}")
            break
    else:
        print("Crypto not found in top 100.")

if __name__ == "__main__":
    get_crypto_price()