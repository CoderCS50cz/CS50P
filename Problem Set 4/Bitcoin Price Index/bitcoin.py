import sys
import requests


if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")


try:
    number = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = o["bpi"]["USD"]["rate_float"]
except requests.RequestException:
    pass


amount = number * rate
print(f"${amount:,.4f}")
