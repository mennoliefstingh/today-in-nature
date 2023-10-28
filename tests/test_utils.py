from datetime import date
from unittest.mock import patch

from today_in_nature.utils import format_date, parse_args


def test_format_date():
    date_ = date(2021, 12, 31)
    assert format_date(date_) == "31/12"
    assert format_date(date_, mmdd=True) == "12/31"


def test_parse_args():
    with patch("sys.argv", ["test", "--language", "en"]):
        args = parse_args()
        assert args.language == "en"

    with patch("sys.argv", ["test", "--language", "en", "--mmdd"]):
        args = parse_args()
        assert args.language == "en"
        assert args.mmdd

    # Assert an exception is thrown when --language ru is passed
    with patch("sys.argv", ["test", "--language", "ru"]):
        try:
            args = parse_args()
        except Exception:
            assert True
        else:
            assert False

    with patch("sys.argv", ["test"]):
        args = parse_args()
        assert args.language == "en"
        assert not args.mmdd
