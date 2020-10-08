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
        

class ConvertDollarsToCurrencyTestCase(TestCase):
        
    @patch('exchange_rate.get_exchange_rate', return_value=1.3)
    def test_nominal_case(self, mock_get_exchange_rate):
        converted = convert_dollars_to_target(5, 'CAD')
        expected_converted = convert(5, 1.3)
        
        self.assertEqual(converted, expected_converted)


if __name__ == '__main__':
    unittest.main()
