import unittest

from app.delivery_fee import delivery_total


class DeliveryFeeTests(unittest.TestCase):
    def test_small_order_pays_delivery(self):
        self.assertEqual(delivery_total(1000), 1400)

    def test_large_order_delivers_free(self):
        self.assertEqual(delivery_total(3000), 3000)
