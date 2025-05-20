from typing import Dict, List

import pytest


@pytest.fixture
def date_state_list() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2024-03-11"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
        {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
        {"id": 615064591, "state": "CANCELED", "date": "2018/07/08"},
    ]


@pytest.fixture
def mylist() -> List[Dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
    ]
