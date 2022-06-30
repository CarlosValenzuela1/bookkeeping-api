from typing import List
import unittest
from unittest.mock import patch
from src.helpers import *
import json


class TestHelpers(unittest.TestCase):
    def test_x(self):
        pass
    # def test_get_invoice_total_example_1(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 2,
    #             "category": "Clothes",
    #             "unit_price_net": "25.00"
    #         },
    #         {
    #             "description": "Holvi hoodie",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "40.00"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 4,
    #             "category": "Posters",
    #             "unit_price_net": "40.00"
    #         }
    #     ]
    #     result = get_invoice_total(all_items)

    # def test_get_invoice_total_example_2(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "2.55"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 1,
    #             "category": "Posters",
    #             "unit_price_net": "2.55"
    #         },
    #         {
    #             "description": "Holvi gift card",
    #             "quantity": 1,
    #             "category": "Gift cards",
    #             "unit_price_net": "43.90"
    #         }
    #     ]
    #     result = get_invoice_total(all_items)

    # def test_get_invoice_total_example_3(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "2.00"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 1,
    #             "category": "Posters",
    #             "unit_price_net": "2.00"
    #         },
    #         {
    #             "description": "Holvi bag",
    #             "quantity": 1,
    #             "category": "Bags",
    #             "unit_price_net": "2.00"
    #         }
    #     ]
    #     result = get_invoice_total(all_items)

    # def test_get_all_categories_example_1(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 2,
    #             "category": "Clothes",
    #             "unit_price_net": "25.00"
    #         },
    #         {
    #             "description": "Holvi hoodie",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "40.00"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 4,
    #             "category": "Posters",
    #             "unit_price_net": "40.00"
    #         }
    #     ]
    #     result = get_all_categories(all_items)

    # def test_get_all_categories_example_2(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "2.55"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 1,
    #             "category": "Posters",
    #             "unit_price_net": "2.55"
    #         },
    #         {
    #             "description": "Holvi gift card",
    #             "quantity": 1,
    #             "category": "Gift cards",
    #             "unit_price_net": "43.90"
    #         }
    #     ]
    #     result = get_all_categories(all_items)

    # def test_get_all_categories_example_3(self):
    #     all_items = [
    #         {
    #             "description": "Holvi T-shirt",
    #             "quantity": 1,
    #             "category": "Clothes",
    #             "unit_price_net": "2.00"
    #         },
    #         {
    #             "description": "Holvi poster",
    #             "quantity": 1,
    #             "category": "Posters",
    #             "unit_price_net": "2.00"
    #         },
    #         {
    #             "description": "Holvi bag",
    #             "quantity": 1,
    #             "category": "Bags",
    #             "unit_price_net": "2.00"
    #         }
    #     ]
    #     result = get_all_categories(all_items)


if __name__ == '__main__':
    unittest.main()
