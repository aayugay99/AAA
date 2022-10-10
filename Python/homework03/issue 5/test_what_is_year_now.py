from what_is_year_now import what_is_year_now
from unittest.mock import patch, MagicMock
import pytest


class Mock1(MagicMock):
    @staticmethod
    def read():
        return '{"$id": "1", "currentDateTime": "2022-10-10T17:25Z"}'


class Mock2(MagicMock):
    @staticmethod
    def read():
        return '{"$id": "2", "currentDateTime": "01.03.2019"}'


class Mock3(MagicMock):
    @staticmethod
    def read():
        return '{"$id": "2", "currentDateTime": "something weird"}'


def test_what_is_year_now_1():
    with patch("urllib.request.urlopen", new_callable=Mock1) as mocked_urlopen:
        assert what_is_year_now() == 2022
        mocked_urlopen.assert_called_once()


def test_what_is_year_now_2():
    with patch("urllib.request.urlopen", new_callable=Mock2) as mocked_urlopen:
        assert what_is_year_now() == 2019
        mocked_urlopen.assert_called_once()


def test_what_is_year_now_3():
    with patch("urllib.request.urlopen", new_callable=Mock3) as mocked_urlopen:
        with pytest.raises(ValueError):
            what_is_year_now()
        mocked_urlopen.assert_called_once()
