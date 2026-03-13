from .client import client

def place_order(symbol, side, order_type, quantity, price=None):
    if order_type == "MARKET":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )
    elif order_type == "LIMIT":
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            timeInForce="GTC",
            quantity=quantity,
            price=price
        )
    elif order_type == "STOP_LIMIT":  # Bonus feature
        return client.futures_create_order(
            symbol=symbol,
            side=side,
            type="STOP_MARKET",
            stopPrice=price,
            quantity=quantity
        )