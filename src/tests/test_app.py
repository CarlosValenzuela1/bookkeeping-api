import unittest
from src.jsons_schema import JsonSchema
from src.tests.app_sample_input import (validation_case_1, validation_case_2,
                                        validation_case_3, validation_case_4,
                                        validation_case_5, validation_case_6,
                                        validation_case_7)


class TestHApp(unittest.TestCase):
    """
    Test class for the methods within app.py
    NOTE: There are no tests for the following conditions, as this can be safely assumed according to the task instructions:
    - Quantity is always a positive integer
    - unit_price is always a string which represents decimal number rounded to two decimal places
    - payment amounts are always positive, and represents decimal numbers rounded to two decimal places
    """

    def test_json_validation_case_0(self):
        """
        Case 0: Empty json from the request, must contain two errors total; due to the missing invoice_lines and the payments property
        """
        expected_result = {'invoice_lines': ['Missing data for required field.'], 'payments': ['Missing data for required field.']}
        result = JsonSchema().validate({})

        self.assertEqual(result, expected_result)

    def test_json_validation_case_1(self):
        """
        Case 1: Using proper json, with all correct properties and types
        """
        expected_result = {}
        result = JsonSchema().validate(validation_case_1)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_2(self):
        """
        Case 2: Missing one of the root properties from json
        """
        expected_result = {'invoice_lines': ['Missing data for required field.']}
        result = JsonSchema().validate(validation_case_2)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_3(self):
        """
        Case 3: Providing empty invoice_lines list
        """
        expected_result = {'invoice_lines': ['Shorter than minimum length 1.']}
        result = JsonSchema().validate(validation_case_3)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_4(self):
        """
        Case 4: Providing empty payments list
        """
        expected_result = {'payments': ['Shorter than minimum length 1.']}
        result = JsonSchema().validate(validation_case_4)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_5(self):
        """
        Case 5: Missing any of the properties from each invoice_line, in this case 'description'
        """
        expected_result = {'invoice_lines': {0: {'description': ['Missing data for required field.']}}}
        result = JsonSchema().validate(validation_case_5)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_6(self):
        """
        Case 6: Missing any of the properties from each payment, in this case 'id'
        """
        expected_result = {'payments': {0: {'id': ['Missing data for required field.']}}}
        result = JsonSchema().validate(validation_case_6)

        self.assertEqual(result, expected_result)

    def test_json_validation_case_7(self):
        """
        Case 7: Containing wrong type, for example quantity being a string instead of an int
        """
        expected_result = {'invoice_lines': {0: {'quantity': ['Not a valid integer.']}}}
        result = JsonSchema().validate(validation_case_7)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
