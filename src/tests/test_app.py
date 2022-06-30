from typing import List
import unittest
from unittest.mock import patch
from src.app import get_bookkipping
import json
# log.basicConfig(
#     level=log.INFO,
#     format='%(asctime)s %(funcName)s %(lineno)d: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S')


class TestApp(unittest.TestCase):

    def test_main_given_example_1(self):
        """
        Example 1 given in the instructions
        """
        f = open('src/tests/example1.json')
        data = json.load(f)
        for i in data.keys():
            print(i)
        f.close()

        expected_result = '1'
        result = get_bookkipping(data)
        self.assertEqual('1', expected_result)

        # with patch('src.main.get_input', return_value=(self.input_formatter(input_string))), \
        #         patch('builtins.print') as mock_print:
        #     main()
        # Asserting the itinerary printed in stdout is the expected
        # mock_print.assert_called_with(expected_itinerary)
        # If you need to see the actual call, uncomment below
        # sys.stdout.write(str(mock_print.call_args) + '\n')

    def input_formatter(self, input_string: str) -> List:
        """
        Makes it easier to create tests' input, by allowing us to use a multi-line string
        """
        customers_preferences = []
        input_list = input_string.split("\n")
        hops, _ = int(input_list[1]), input_list[2]
        # 1st line is an empty \n, 2nd belong to hops, 3rd to the number of customers, 4th... until penultimate are the customer preferences, last item is an empty \n
        for pref in input_list[3:-1]:
            customers_preferences.append(pref.strip().split(", "))
        return hops, customers_preferences


if __name__ == '__main__':
    unittest.main()
