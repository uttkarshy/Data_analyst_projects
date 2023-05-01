import requests

url = "https://currency-exchange.p.rapidapi.com/exchange"

from_currency = input("Enter the currency you want to convert from: ")
to_currency = input("Enter the currency you want to convert to: ")
amount = float(input("Enter the amount you want to convert: "))

querystring = {"from": from_currency.upper(), "to": to_currency.upper(), "q": amount}

headers= {
    'X-RapidAPI-Key': '811cd18798msh49ff93aa4168bc9p1726f4jsne4d12f9bd6a2',
    'X-RapidAPI-Host': 'currency-converter5.p.rapidapi.com'
}

response = requests.request("GET", url, headers=headers, params=querystring)

if response.ok:
    exchange_rate = float(response.text)
    converted_amount = amount * exchange_rate
    print(f"{amount} {from_currency.upper()} is equal to {converted_amount:.2f} {to_currency.upper()}")
else:
    print("Error: Could not get exchange rate.")
