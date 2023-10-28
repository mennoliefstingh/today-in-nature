# import pytz
# from datetime import datetime
# from today_in_nature.utils import ensure_dir, parse_args, print_box
# import requests
# import json
# import os


# TITLE_STR = {"en": "TODAY IN NATURE", "nl": "VANDAAG IN DE NATUUR"}


# def main():
#     args = parse_args()

#     amsterdam_tz = pytz.timezone("Europe/Amsterdam")
#     date = datetime.now(amsterdam_tz)

#     cache_dir = os.path.expanduser("~/.cache/today_in_nature")
#     ensure_dir(cache_dir)

#     cache_path = cache_dir + f"/{date.strftime('%d_%m_%Y')}.json"

#     if os.path.exists(os.path.expanduser(cache_path)):
#         with open(os.path.expanduser(cache_path)) as f:
#             data = json.load(f)
#     else:
#         try:
#             response = requests.get("https://menno.ai/today-in-nature")
#         except requests.exceptions.ConnectionError:
#             print("Connection to menno.ai failed.")
#             return
#         data = response.json()
#         with open(cache_path, "x") as f:
#             json.dump(data, f)

#     if args.mmdd:
#         date_str = date.strftime("%m/%d")
#     else:
#         date_str = date.strftime("%d/%m")

#     print_box(title=f"{date_str} {TITLE_STR[args.language]}", content=data[args.language])

from datetime import datetime

from today_in_nature.data_loader import get_data
from today_in_nature.utils import format_date, parse_args, print_box

TITLE_STR = {"en": "TODAY IN NATURE", "nl": "VANDAAG IN DE NATUUR"}


def main():
    """
    Main function that retrieves data and prints it in a formatted box.

    Returns:
        None
    """
    args = parse_args()
    data = get_data()

    if data is None:
        return

    title = TITLE_STR.get(data[args.language], TITLE_STR[args.language])
    date_str = format_date(datetime.now(), args.mmdd)
    fact = data[args.language]

    print_box(f"{date_str} {title}", fact)


if __name__ == "__main__":
    main()
