import unittest
from bot.validators import validate_inputs

class TestValidators(unittest.TestCase):
    def test_valid_market_order(self):
        # Should not raise an error
        self.assertIsNone(validate_inputs("BTCUSDT", "BUY", "MARKET", 0.01))

    def test_invalid_side(self):
        # Invalid side should raise ValueError
        with self.assertRaises(ValueError):
            validate_inputs("BTCUSDT", "HOLD", "MARKET", 0.01)

    def test_limit_without_price(self):
        # LIMIT order without price should raise ValueError
        with self.assertRaises(ValueError):
            validate_inputs("BTCUSDT", "SELL", "LIMIT", 0.01)

    def test_stop_limit_without_price(self):
        # STOP_LIMIT order without price should raise ValueError
        with self.assertRaises(ValueError):
            validate_inputs("BTCUSDT", "SELL", "STOP_LIMIT", 0.01)

if __name__ == "__main__":
    unittest.main()