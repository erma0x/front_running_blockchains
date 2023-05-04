import time
from binance.client import Client

api_key = 'your_api_key'
api_secret = 'your_api_secret'

client = Client(api_key, api_secret)

symbol = 'BTCUSDT'
quantity = 0.01
price = 0.0

while True:
    orders = client.get_order_book(symbol=symbol)
    bid_price = float(orders['bids'][0][0])
    ask_price = float(orders['asks'][0][0])
    if bid_price > price:
        price = bid_price
        client.order_limit_sell(symbol=symbol, quantity=quantity, price=price)
    elif ask_price < price:
        price = ask_price
        client.order_limit_buy(symbol=symbol, quantity=quantity, price=price)
    time.sleep(1)

