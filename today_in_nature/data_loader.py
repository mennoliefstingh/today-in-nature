import json
import os
from datetime import datetime

import pytz
import requests

CACHE_DIR = os.path.expanduser("~/.cache/today_in_nature")


def ensure_dir(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)


def get_data():
    ensure_dir(CACHE_DIR)
    amsterdam_tz = pytz.timezone("Europe/Amsterdam")
    date = datetime.now(amsterdam_tz)
    cache_path = f"{CACHE_DIR}/{date.strftime('%d_%m_%Y')}.json"

    if os.path.exists(cache_path):
        with open(cache_path) as f:
            data = json.load(f)
    else:
        try:
            response = requests.get("https://menno.ai/today-in-nature")
        except requests.exceptions.ConnectionError:
            print("Connection to menno.ai failed.")
            return None
        data = response.json()
        with open(cache_path, "x") as f:
            json.dump(data, f)

    return data
