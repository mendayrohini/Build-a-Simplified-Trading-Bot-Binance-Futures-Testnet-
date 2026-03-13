def validate_inputs(symbol, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")
    if quantity <= 0:
        raise ValueError("Quantity must be positive")
    if order_type in ["LIMIT", "STOP_LIMIT"] and price is None:
        raise ValueError("Price required for LIMIT/STOP_LIMIT orders")