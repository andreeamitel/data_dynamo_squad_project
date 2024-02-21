import copy


def dim_currency(currency_table_data):
    if currency_table_data == {}:
        return {}
    currency_dict = copy.deepcopy(currency_table_data)
    dim_curr = {"dim_currency": []}

    for currency in currency_dict['currency']:
        if currency['currency_code'] == 'GBP':
            currency_name = 'Great British Pound'
        elif currency['currency_code'] == 'USD':
            currency_name = 'United States Dollar'
        elif currency['currency_code'] == 'EUR':
            currency_name = 'Euro'
        dim_curr['dim_currency'].append({
            'currency_id': currency['currency_id'],
            'currency_code': currency['currency_code'],
            'currency_name': currency_name,
        }
        )

    return dim_curr
