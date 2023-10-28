import os

from today_in_nature.data_loader import get_data

CACHE_DIR = os.path.expanduser("~/.cache/today_in_nature")


def test_get_data():
    # Test that the function returns a dictionary
    assert isinstance(get_data(), dict)

    # Test that the dictionary has the expected keys
    expected_keys = ["date", "en", "nl"]
    assert all(key in get_data() for key in expected_keys)
