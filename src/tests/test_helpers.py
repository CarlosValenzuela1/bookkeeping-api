import json
import unittest
from decimal import Decimal
from src.helpers import (calculate_bookkeeping, calculate_categorisations,
                         calculate_percentage_per_category,
                         calculate_total_per_category, get_categories, rounder,
                         sum_products_total)
from src.tests.helpers_sample_inputs import (bookkipping_case_1,
                                             bookkipping_case_2,
                                             bookkipping_case_3,
                                             bookkipping_case_4,
                                             bookkipping_case_5,
                                             bookkipping_case_6,
                                             bookkipping_case_7)


class TestHelpers(unittest.TestCase):
    """
    Bookkipping main function tests.
    Sample input for the main function was not used inline for better readability, all the other methods will include it.
    """

    def test_bookkipping_case_1(self):
        """
        Case: Full code execution with example 1 provided by the instructions
        """
        expected_result = json.dumps([{"id": 1, "categorisations": [{"category": "Clothes", "net_amount": "18.00"}, {"category": "Posters", "net_amount": "32.00"}]},
                                     {"id": 2, "categorisations": [{"category": "Clothes", "net_amount": "72.00"}, {"category": "Posters", "net_amount": "128.00"}]}])
        result = calculate_bookkeeping(bookkipping_case_1)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_2(self):
        """
        Case: Full code execution with example 2 provided by the instructions
        """
        expected_result = json.dumps([{"id": 3, "categorisations": [{"category": "Clothes", "net_amount": "0.16"}, {
                                     "category": "Posters", "net_amount": "0.16"}, {"category": "Gift cards", "net_amount": "2.68"}]}])
        result = calculate_bookkeeping(bookkipping_case_2)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_3(self):
        """
        Case: Full code execution with example 3 provided by the instructions
        """
        expected_result = json.dumps([{"id": 4, "categorisations": [{"category": "Clothes", "net_amount": "1.48"}, {
                                     "category": "Posters", "net_amount": "1.48"}, {"category": "Bags", "net_amount": "1.49"}]}])
        result = calculate_bookkeeping(bookkipping_case_3)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_4(self):
        """
        Case: Full code execution with 1 invoice_line, 1 category, 1 quantity and 1 payment
        """
        expected_result = json.dumps([{"id": 4, "categorisations": [{"category": "Clothes", "net_amount": "4.45"}]}])
        result = calculate_bookkeeping(bookkipping_case_4)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_5(self):
        """
        Case: Full code execution with 2 invoice_line, 2 categories, varied quantity and 1 payment
        """
        expected_result = json.dumps([{"id": 4, "categorisations": [{"category": "Clothes", "net_amount": "1.11"}, {"category": "Posters", "net_amount": "3.34"}]}])
        result = calculate_bookkeeping(bookkipping_case_5)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_6(self):
        """
        Case: Full code execution with 2 invoice_line,  1 categories, varied quantity and 1 payment.
        To check for repeated category and same item with varied prices on each of the invoice_lines
        """
        expected_result = json.dumps([{"id": 4, "categorisations": [{"category": "Clothes", "net_amount": "4.45"}]}])
        result = calculate_bookkeeping(bookkipping_case_6)

        self.assertEqual(result, expected_result)

    def test_bookkipping_case_7(self):
        """
        Case: Full code execution with 2 invoice_line,  1 categories, varied quantity and 2 payment.
        """
        expected_result = json.dumps([{"id": 4, "categorisations": [{"category": "Clothes", "net_amount": "0.81"}, {"category": "Posters", "net_amount": "3.64"}]},
                                     {"id": 5, "categorisations": [{"category": "Clothes", "net_amount": "1.03"}, {"category": "Posters", "net_amount": "4.66"}]}])
        result = calculate_bookkeeping(bookkipping_case_7)

        self.assertEqual(result, expected_result)

    """
    get_categories() function tests
    """

    def test_get_categories_case_1(self):
        """
        Case: Given a list of products with 1 'Category'
        """
        get_categories_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 2,
                "category": "Clothes",
                "unit_price_net": "25.00"
            }
        ]
        expected_result = {'Clothes'}
        result = get_categories(get_categories_sample)

        self.assertEqual(result, expected_result)

    def test_get_categories_case_2(self):
        """
        Case: Given a list of products with multiple 'Category'
        """
        get_categories_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 2,
                "category": "Clothes",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi Bag",
                "quantity": 1,
                "category": "Bag",
                "unit_price_net": "40.00"
            }
        ]
        expected_result = {'Clothes', 'Bag'}
        result = get_categories(get_categories_sample)

        self.assertEqual(result, expected_result)

    def test_get_categories_case_3(self):
        """
        Case: Given a list of products with multiple repeated 'Category'
        """
        get_categories_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 2,
                "category": "Clothes",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi hoodie",
                "quantity": 1,
                "category": "Clothes",
                "unit_price_net": "40.00"
            }
        ]
        expected_result = {'Clothes'}
        result = get_categories(get_categories_sample)

        self.assertEqual(result, expected_result)

    def test_get_categories_case_4(self):
        """
        Case: Given a list of products with multiple repeated 'Category' but different case spelling (Lower case, upper case, etc).
        """
        get_categories_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 2,
                "category": "CLOTHES",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi hoodie",
                "quantity": 1,
                "category": "ClOtHEs",
                "unit_price_net": "40.00"
            }
        ]
        expected_result = {'Clothes'}
        result = get_categories(get_categories_sample)

        self.assertEqual(result, expected_result)

    """
    sum_products_total() function tests
    """

    def test_sum_products_total_case_1(self):
        """
        Case: Given a list of products with 1 'category', 1 'quantity'
        """
        sum_products_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 1,
                "category": "Clothes",
                "unit_price_net": "25.00"
            }
        ]
        expected_result = Decimal("25.00")
        result = sum_products_total(sum_products_sample)

        self.assertEqual(result, expected_result)

    def test_sum_products_total_case_2(self):
        """
        Case: Given a list of products with 1 'category', multiple 'quantity'
        """
        sum_products_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 5,
                "category": "Clothes",
                "unit_price_net": "25.00"
            }
        ]
        expected_result = Decimal("125.00")
        result = sum_products_total(sum_products_sample)

        self.assertEqual(result, expected_result)

    def test_sum_products_total_case_3(self):
        """
        Case: Given a list of products with multiple 'category', multiple 'quantity'
        """
        sum_products_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 5,
                "category": "Clothes",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi Bag",
                "quantity": 3,
                "category": "Bag",
                "unit_price_net": "10.00"
            }
        ]
        expected_result = Decimal("155.00")
        result = sum_products_total(sum_products_sample)

        self.assertEqual(result, expected_result)

    def test_sum_products_total_case_4(self):
        """
        Case: Given a list of products with multiple 'category' (including repeated categories with different case)
        and multiple 'quantity' and different value for the same product
        """
        sum_products_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 5,
                "category": "CLOTHES",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi Bag",
                "quantity": 3,
                "category": "Bag",
                "unit_price_net": "10.00"
            },
            {
                "description": "HOLVI BAG",
                "quantity": 7,
                "category": "Bag",
                "unit_price_net": "12.00"
            }
        ]
        expected_result = Decimal("239.00")
        result = sum_products_total(sum_products_sample)

        self.assertEqual(result, expected_result)

    """
    calculate_total_per_category() function tests
    """

    def test_calculate_total_per_category_case_1(self):
        """
        Case: Given a list of products and a list of all available categories, simple test
        """
        products_sample = [
            {
                "description": "Holvi Bag",
                "quantity": 5,
                "category": "Bag",
                "unit_price_net": "25.00"
            }
        ]
        categories_sample = {'Bag'}
        expected_result = {'Bag': Decimal('125.00')}
        result = calculate_total_per_category(products_sample, categories_sample)

        self.assertEqual(result, expected_result)

    def test_calculate_total_per_category_case_2(self):
        """
        Case: Given a list of products and a list of all available categories and repeated category and description with different price
        """
        products_sample = [
            {
                "description": "Holvi T-shirt",
                "quantity": 5,
                "category": "Clothes",
                "unit_price_net": "25.00"
            },
            {
                "description": "Holvi Bag",
                "quantity": 3,
                "category": "Bag",
                "unit_price_net": "10.00"
            },
            {
                "description": "HOLVI BAG",
                "quantity": 7,
                "category": "Bag",
                "unit_price_net": "12.00"
            }
        ]
        categories_sample = {'Clothes', 'Bag'}
        expected_result = {'Clothes': Decimal('125.00'), 'Bag': Decimal('114.00')}
        result = calculate_total_per_category(products_sample, categories_sample)

        self.assertEqual(result, expected_result)

    """
    calculate_percentage_per_category() function tests
    """

    def test_calculate_percentage_per_category_case_1(self):
        """
        Case: Given a list of 1 total amount per category and the total sum amount of all products. Percentage = 100%
        """
        total_per_category_sample = {'Clothes': Decimal('10.00')}
        products_total_sample = Decimal('10.00')
        expected_result = {'Clothes': Decimal('1.00')}
        result = calculate_percentage_per_category(total_per_category_sample, products_total_sample)

        self.assertEqual(result, expected_result)

    def test_calculate_percentage_per_category_case_2(self):
        """
        Case: Given a list of 2 total amount per category and the total sum amount of all products. Percentage = 50%
        """
        total_per_category_sample = {'Clothes': Decimal('50.00'), 'Posters': Decimal('50.00')}
        products_total_sample = Decimal('100.00')
        expected_result = {'Clothes': Decimal('0.50'), 'Posters': Decimal('0.50')}
        result = calculate_percentage_per_category(total_per_category_sample, products_total_sample)

        self.assertEqual(result, expected_result)

    def test_calculate_percentage_per_category_case_3(self):
        """
        Case: Given a list of 3 total amount per category and the total sum amount of all products. Percentage = 33.33..%
        """
        total_per_category_sample = {'Clothes': Decimal('33.33'), 'Bag': Decimal('33.33'), 'Posters': Decimal('33.33')}
        products_total_sample = Decimal('100.00')
        expected_result = {'Clothes': Decimal('0.3333'), 'Bag': Decimal('0.3333'), 'Posters': Decimal('0.3333')}
        result = calculate_percentage_per_category(total_per_category_sample, products_total_sample)

        self.assertEqual(result, expected_result)

    """
    calculate_categorisations() function tests
    """

    def test_calculate_categorisations_case_1(self):
        """
        Case: Given 2 categories, and 1 payment only
        """

        payments_sample = [{"id": 1, "amount": "50.00"}, {"id": 2, "amount": "200.00"}]
        percentage_per_category_sample = {'Clothes': Decimal('33.33'), 'Bag': Decimal('33.33')}
        expected_result = [{'id': 1, 'categorisations': [{'category': 'Clothes', 'net_amount': '1666.50'}, {'category': 'Bag', 'net_amount': '-1616.50'}]},
                           {'id': 2, 'categorisations': [{'category': 'Clothes', 'net_amount': '6666.00'}, {'category': 'Bag', 'net_amount': '-6466.00'}]}]
        result = calculate_categorisations(payments_sample, percentage_per_category_sample)

        self.assertEqual(result, expected_result)

    def test_calculate_categorisations_case_2(self):
        """
        Case: Given multiple categories and multiple payments
        """

        payments_sample = [{"id": 1, "amount": "50.00"}, {"id": 2, "amount": "200.00"}]
        percentage_per_category_sample = {'Clothes': Decimal('33.33'), 'Bag': Decimal('33.33'), 'Posters': Decimal('33.33')}
        expected_result = [{'id': 1, 'categorisations': [{'category': 'Clothes', 'net_amount': '1666.50'}, {'category': 'Bag', 'net_amount': '1666.50'}, {'category': 'Posters', 'net_amount': '-3283.00'}]},
                           {'id': 2, 'categorisations': [{'category': 'Clothes', 'net_amount': '6666.00'}, {'category': 'Bag', 'net_amount': '6666.00'}, {'category': 'Posters', 'net_amount': '-13132.00'}]}]
        result = calculate_categorisations(payments_sample, percentage_per_category_sample)

        self.assertEqual(result, expected_result)

    """
    rounder() function tests
    """

    def test_rounder_case_1(self):
        """
        Case: Requiring rounding
        """
        total_amount_sample = "100.00"
        current_amount_sample = "99.99"
        estimated_amount_sample = Decimal("99.99")
        expected_result = '100.00'
        result = rounder(total_amount_sample, current_amount_sample, estimated_amount_sample)

        self.assertEqual(result, expected_result)

    def test_rounder_case_2(self):
        """
        Case: Rounding is not required
        """
        total_amount_sample = "100.00"
        current_amount_sample = "100.00"
        estimated_amount_sample = Decimal("100.00")
        expected_result = '100.00'
        result = rounder(total_amount_sample, current_amount_sample, estimated_amount_sample)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
