import typer
from bot.orders import place_order
from bot.validators import validate_inputs
from loguru import logger

app = typer.Typer()

@app.command()
def order(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    try:
        validate_inputs(symbol, side, order_type, quantity, price)
        response = place_order(symbol, side, order_type, quantity, price)
        logger.info(f"Order Response: {response}")
        print(" ✅ Order placed successfully!")
        print(f"Order ID: {response['orderId']}, Status: {response['status']}")
    except Exception as e:
        logger.error(f"Error placing order: {e}")
        print("❌ Failed to place order")

if __name__ == "__main__":
    app()
