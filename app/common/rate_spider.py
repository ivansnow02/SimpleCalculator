import json
import time
import os
from urllib import request


def save():
    try:
        api_url = "https://v6.exchangerate-api.com/v6/2188cc1345d2d391da8fc7a2/latest/CNY"
        req = request.Request(api_url)
        data = {}
        with request.urlopen(req) as response:
            json_data = json.loads(response.read().decode('utf-8'))
            data = json_data
        if not os.path.exists("data/rate.json"):
            os.mkdir("data")
        with open("data/rate.json", "w") as f:
            json.dump(data, f)

    except Exception as e:
        return e


def load():
    try:
        with open("data/rate.json", "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return e


def get_rate() -> dict:
    save()
    data = load()
    update_time = data["time_next_update_unix"]
    if int(time.time()) > int(update_time):
        save()
        data = load()
    return data["conversion_rates"]


if __name__ == '__main__':
    # save()
    print(get_rate())
