""" Uses exchangeratesapi.io to get exchange rates
Validation, error handling omitted for clarity.  """


import requests

def main():
    currency = get_target_currency()
    dollars = get_dollar_amount()
    converted = convert_dollars_to_target(dollars, currency)
    
    if converted != None:
        display_result(dollars, currency, converted)
    
def get_target_currency():
    """ Get target currency, and return as uppercase symbol. """
    while True:
        currency = input('Enter target currency code e.g. EUR, CAD: ')
        
        # only accept three-letter currency codes
        if len(currency) == 3 and currency.isalpha():
            return currency.upper()
        else:
            print('Invalid currency code')

def get_dollar_amount():
    """ Get number of dollars. """
    while True:
        try:
            return float(input('Enter amount of dollars to convert: '))
        
        # handle exception when given non-numeric input
        except ValueError:
            print('Invalid dollar value')

def convert_dollars_to_target(dollars, target_currency):
    """ Convert amount of dollars to target currency """
    exchange_rate = get_exchange_rate(target_currency)
    
    if exchange_rate != None:
        return convert(dollars, exchange_rate)
    else:
        return None

def get_exchange_rate(currency):
    """ Call API and extra data from response """
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate 

def request_rates(currency):
    """ Perform API request, return response. """
    params = {'base': 'USD', 'symbols': currency}
    url = 'https://api.exchangeratesapi.io/latest'
    
    try:
        response = requests.get(url, params=params).json()
        
        # if response has an 'error' field, return None
        if 'error' not in response:
            return response
        else:
            print(f'Couldn\'t find an exchange rate for {currency}. Cannot get exchange rate for {currency}.')
            return None
        
    # handle exception if connection with API fails
    except requests.exceptions.ConnectionError as e:
        print(f'Couldn\'t establish connection with API. Cannot get exchange rate for {currency}.')
        return None

def extract_rate(rates, currency):
    """ Process the JSON response from the API, extract rate data. """
    
    # check if response from request_rates was None
    if rates != None:
        return rates['rates'][currency]
    else:
        return None


def convert(amount, exchange_rate):
    """ Convert using the given exchange rate """
    return amount * exchange_rate

def display_result(dollars, currency, converted):
    """ Format and display the result """
    print(f'${dollars:.2f} is equivalent to {currency} {converted:.2f}')


if __name__ == '__main__':
    main()
