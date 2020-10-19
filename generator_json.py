from random import randint, choices
from datetime import datetime as dt
from requests import post
import json


def create_json():

    person = ['José', 'Heitor', 'Maria', 'Lopez', 'Ricardo']
    state = ['SP', 'RJ', 'GO', 'MT', 'AM', 'SC', 'DF']

    payload = {
        'NAME': choices(person)[0],
        'DOC_NUMER': randint(1, 1000000000),
        'DOC_ITEM': randint(0, 10000),
        'STATE_ID': choices(state)[0],
        'CREATE_AT': dt.now().strftime('%Y-%m-%d'),
    }

    return json.dumps(payload)


def output_json(data):

    try:

        headers = {'content-type': 'application/json'}
        url = 'http://localhost:5000/contentListener'

        response = post(url, headers=headers, data=data)

        response.raise_for_status()

        print(f'Dados enviado com sucesso!\n{data}')

    except Exception as error:
        raise SystemExit(error)


if __name__ == "__main__":
    data_json = create_json()
    output_json(data_json)
