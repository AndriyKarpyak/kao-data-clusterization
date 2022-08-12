# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import time

import pandas as pandas
import requests

INTERVAL_BETWEEN_REQUESTS_SECONDS = 10


def gen_params(code, date='2021-12-01', taxpayer_type=''):
    return {
        'budgetType': 'consolidated',
        'date': date,
        'region': '',
        'kved': code,
        'budgetCode': '',
        'taxpayerType': taxpayer_type,
        'taxpayerStatus': '',
        'taxSystem': '',
        'vipTaxpayer': '',
        'legalForm': '',
    }


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    kveds = {
        "_J61": "Телекомунікації (електрозв'язок)",
        "_J58": "Видавнича діяльність",
        "K72": "КВЕД-2005: Дiяльнiсть у сферi iнформатизацiї",
        "DE22": "КВЕД-2005: Видавнича та полiграфiчна дiяльнiсть, тиражування записаних носiїв iнформацiї",
        "_J63": "Надання інформаційних послуг",
        "_J62": "Комп'ютерне програмування, консультування та пов'язана з ними діяльність",
        "_J59": "Виробництво кіно- та відеофільмів, телевізійних програм, видання звукозаписів",
        "_J60": "Діяльність у сфері радіомовлення та телевізійного мовлення",
    }
    data = {}
    columns = ['Регіон']
    kved_index = 0

    for kved_code, kved_name in kveds.items():

        print('Begin processing kved [{}]'.format(kved_name))

        print('  Requesting cumulative information...')
        r = requests.get(
            'https://map.tax.gov.ua/api/taxes/revenue/cumulative/by/none/ranking', params=gen_params(kved_code))
        print('    Received cumulative information! [{}]'.format(r.json()))

        columns.extend([kved_name, 'Надходження', 'На мешканця'])
        if r.json()['items']:
            for item in r.json()['items']:

                if item['label'] not in data:
                    data[item['label']] = [math.nan] * (len(kveds) * 5)

                value = item['value'] if item['value'] else math.nan
                per_capita = item['perCapita'] if item['perCapita'] else math.nan
                data[item['label']][kved_index + 1] = value
                data[item['label']][kved_index + 2] = per_capita

        time.sleep(INTERVAL_BETWEEN_REQUESTS_SECONDS)
        print('  Requesting information for legal_entities ...')
        r = requests.get(
            'https://map.tax.gov.ua/api/taxes/revenue/cumulative/by/none/ranking',
            params=gen_params(kved_code, taxpayer_type='legal_entities'))
        print('    Received information for legal_entities! [{}]'.format(r.json()))

        columns.append('Юридичні особи')
        if r.json()['items']:
            for item in r.json()['items']:
                if item['value']:
                    data[item['label']][kved_index + 3] = item['value']

        time.sleep(INTERVAL_BETWEEN_REQUESTS_SECONDS)
        print('  Requesting information for individuals ...')
        r = requests.get(
            'https://map.tax.gov.ua/api/taxes/revenue/cumulative/by/none/ranking',
            params=gen_params(kved_code, taxpayer_type='individuals'))
        print('    Received information for individuals! [{}]'.format(r.json()))

        columns.append('Фізичні особи')
        if r.json()['items']:
            for item in r.json()['items']:
                if item['value']:
                    data[item['label']][kved_index + 4] = item['value']

        print('Complete processing kved [{}]'.format(kved_name))
        time.sleep(INTERVAL_BETWEEN_REQUESTS_SECONDS)

        kved_index = kved_index + 5

    print('')
    print('-----------------------')
    print('Columns: {}'.format(len(columns)))
    print(columns)

    data_mx = []
    for region_name, stats in data.items():
        row = [region_name] + stats
        data_mx.append(row)
        print('Row length: {}'.format(len(row)))
        print(row)

    df1 = pandas.DataFrame(data_mx, columns=columns)
    df1.to_excel("output/доходи.xlsx")

    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
