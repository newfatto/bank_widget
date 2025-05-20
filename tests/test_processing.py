import pytest

from src.processing import filter_by_state, sort_by_date

# Тестирование функции filter_by_state()


def test_filter_by_state(mylist: list[dict]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(mylist, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
    ]


def test_filter_by_state_no_state(mylist: list[dict]) -> None:
    """Тестирование фильтрации списка словарей при отсутствии параметра state"""
    assert filter_by_state(mylist) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
            ],
        ),
    ],
)
def test_filter_by_state_any_state(mylist: list[dict], state: str, expected: list[dict]) -> None:
    """Тестирование при различных параметрах state"""
    assert filter_by_state(mylist, state) == expected


def test_filter_by_state_incorrect_state(mylist: list[dict]) -> None:
    """Тестирование возникновения ошибки при некорректном параметре state"""
    with pytest.raises(ValueError):
        filter_by_state(mylist, "ЗНАЧЕНИЕ")


def test_filter_by_state_incorrect_list() -> None:
    """Тестирование возникновения ошибки при передаче некорректного списка"""
    with pytest.raises(ValueError):
        filter_by_state([])


# Тестирование функции sort_by_date()


def test_sort_by_date(mylist: list[dict]) -> None:
    """Проверка функции сортировки по дате (без определения параметра - убывание)"""
    assert sort_by_date(mylist) == [
        {"id": 41428829, "state": "EXECUTED", "date": "03.07.2019"},
        {"id": 615064591, "state": "CANCELED", "date": "14.10.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
    ]


def test_sort_by_date_reverse(mylist: list[dict]) -> None:
    """Проверка функции сортировки по дате (по возрастанию)"""
    assert sort_by_date(mylist, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
        {"id": 615064591, "state": "CANCELED", "date": "14.10.2018"},
        {"id": 41428829, "state": "EXECUTED", "date": "03.07.2019"},
    ]


def test_sort_by_date_diff_date(date_state_list: list[dict]) -> None:
    """Проверка функции сортировки c различными форматами дат"""
    assert sort_by_date(date_state_list) == [
        {"id": 41428829, "state": "EXECUTED", "date": "11.03.2024"},
        {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
        {"id": 615064591, "state": "CANCELED", "date": "08.07.2018"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
    ]


def test_sort_by_date_same_date() -> None:
    """Проверка функции сортировки c одинаковой датой"""
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
            {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
            {"id": 615064591, "state": "CANCELED", "date": "2018/07/08"},
        ]
    ) == [
        {"id": 594226727, "state": "CANCELED", "date": "12.09.2018"},
        {"id": 615064591, "state": "CANCELED", "date": "08.07.2018"},
        {"id": 41428829, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
    ]


def test_sort_by_date_incorrect_list() -> None:
    """Тестирование возникновения ошибки при передаче пустого списка"""
    with pytest.raises(ValueError):
        sort_by_date([])


def test_sort_by_date_incorrect_date() -> None:
    """Тестирование возникновения ошибки при передаче списка без дат"""
    with pytest.raises(KeyError):
        sort_by_date(
            [
                {"id": 615064591, "state": "CANCELED"},
                {"id": 939719570, "state": "EXECUTED"},
                {"id": 594226727, "state": "CANCELED"},
                {"id": 41428829, "state": "EXECUTED"},
            ]
        )
