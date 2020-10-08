import unittest
from unittest import TestCase
from unittest.mock import patch
from exchange_rate import *


class GetTargetCurrencyTestCase(TestCase):
    
    @patch('builtins.input', return_value='hkd')
    def test_nominal_case(self, mock_input):
        currency = get_target_currency()
        expected_currency = mock_input.return_value.upper()
        self.assertEqual(currency, expected_currency)
        

class GetDollarAmountTestCase(TestCase):
    
    @patch('builtins.input', return_value='4.99')
    def test_nominal_case(self, mock_input):
        dollar_amount = get_dollar_amount()
        expected_dollar_amount = float(mock_input.return_value)
        self.assertEqual(dollar_amount, expected_dollar_amount)


if __name__ == '__main__':
    unittest.main()
