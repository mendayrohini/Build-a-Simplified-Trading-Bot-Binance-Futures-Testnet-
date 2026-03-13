import unittest
from unittest.mock import patch
from bot.orders import place_order

class TestOrders(unittest.TestCase):
    @patch("bot.orders.client.futures_create_order")
    def test_market_order(self, mock_order):
        mock_order.return_value = {"orderId": 1, "status": "FILLED"}
        response = place_order("BTCUSDT", "BUY", "MARKET", 0.01)
        self.assertEqual(response["status"], "FILLED")

    @patch("bot.orders.client.futures_create_order")
    def test_limit_order(self, mock_order):
        mock_order.return_value = {"orderId": 2, "status": "NEW"}
        response = place_order("BTCUSDT", "SELL", "LIMIT", 0.01, price=60000)
        self.assertEqual(response["status"], "NEW")

    @patch("bot.orders.client.futures_create_order")
    def test_stop_limit_order(self, mock_order):
        mock_order.return_value = {"orderId": 3, "status": "NEW"}
        response = place_order("BTCUSDT", "SELL", "STOP_LIMIT", 0.01, price=58000)
        self.assertEqual(response["status"], "NEW")

if __name__ == "__main__":
    unittest.main()