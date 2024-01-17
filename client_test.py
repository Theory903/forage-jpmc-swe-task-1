import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def assertGetDataPoint(self, quote):
        expected_result = (
            quote['stock'],
            quote['top_bid']['price'],
            quote['top_ask']['price'],
            (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        )
        result = getDataPoint(quote)
        self.assertEqual(result, expected_result)

    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate through quotes and test the getDataPoint method
        for quote in quotes:
            self.assertGetDataPoint(quote)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        # Iterate through quotes and test the getDataPoint method
        for quote in quotes:
            self.assertGetDataPoint(quote)

    def assertGetRatio(self, price_a, price_b, expected_result):
        result = getRatio(price_a, price_b)
        self.assertEqual(result, expected_result)

    def test_getRatio(self):
        # Test cases for the getRatio method
        # For example:
        self.assertGetRatio(120.0, 110.0, 1.0909090909090908)

        # Additional test cases for getRatio
        self.assertIsNone(self.assertGetRatio(120.0, 0, None))  # Expecting None for division by zero case
        self.assertEqual(self.assertGetRatio(0, 110.0, 0), None)  # Expecting 0 for zero numerator case  # Expecting
        # 0 for
        # zero numerator case


if __name__ == '__main__':
    unittest.main()
