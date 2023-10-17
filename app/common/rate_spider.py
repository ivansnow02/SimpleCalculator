import json
import time
from urllib import request


def save():
    try:
        api_url = "https://v6.exchangerate-api.com/v6/2188cc1345d2d391da8fc7a2/latest/CNY"
        req = request.Request(api_url)
        data = {}
        with request.urlopen(req) as response:
            json_data = json.loads(response.read().decode('utf-8'))
            data = json_data['conversion_rates']
            data['update_time'] = json_data['time_next_update_unix']
        with open('../resource/conversion_rates.json', 'w') as f:
            json.dump(data, f)
    except Exception as e:
        return e


def load():
    try:
        with open('../resource/conversion_rates.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        return e


def get_rate():
    try:
        data = load()
        if data['update_time'] < int(time.time()) or data == {} or data['update_time'] is None:
            save()
            data = load()
        return data
    except Exception as e:
        return e


if __name__ == '__main__':
    # save()
    print(get_rate())
