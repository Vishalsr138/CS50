import requests
import sys
import json

if len(sys.argv) < 2:
    sys.exit(1)

try:
    coins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=904f547777614204d85fe1d6f737dc8c4678d64a7edff490e883438cd8d3759b")
except requests.RequestException:
    print("request error")

o = response.json()

price = float(o["data"]["priceUsd"])
cost= float(coins)*price

print(f"${cost:,.4f}")

