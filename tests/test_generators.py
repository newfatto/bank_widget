from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# Проверка работы функции filter_by_currency


@pytest.fixture
def transactions() -> list[dict]:
    """Фикстура, предоставляющая список транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "currency_code": "USD",
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "currency_code": "USD",
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "currency_code": "USD",
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 42,
            "state": "EXECUTED",
            "date": "2024-01-01T00:00:00.000000",
            "currency_code": "EUR",
            "description": "Перевод организации",
            "from": "Some Account",
            "to": "Another Account",
        },
        {
            "id": 43,
            "state": "EXECUTED",
            "date": "2024-01-01T00:00:00.000000",
            "currency_code": "EUR",
            "description": "Перевод со счета на счет",
            "from": "Some Account",
            "to": "Another Account",
        },
    ]


def test_filter_by_currency(transactions: List[Dict]) -> None:
    """Проверка корректности работы функции при работе с заданной валютой"""
    usd_transactions = [t for t in transactions if t["currency_code"] == "USD"]
    gen = filter_by_currency(transactions, "USD")

    for expected_transaction in usd_transactions:
        assert next(gen) == expected_transaction

    with pytest.raises(StopIteration):
        next(gen)


def test_filter_by_currency_incorrect(transactions: list[dict]) -> None:
    """Тестирование возникновения ошибки при передаче некорректной валюты"""
    with pytest.raises(StopIteration):
        iterator = filter_by_currency(transactions, "TNG")
        next(iterator)


def test_filter_by_currency_empty_list(invalid_transactions: list[dict]) -> None:
    """Тестирование возникновения ошибки при передаче пустого списка"""
    with pytest.raises(ValueError):
        iterator = filter_by_currency(invalid_transactions, "USD")
        next(iterator)


def test_filter_by_currency_invalid_list() -> None:
    """Тестирование возникновения ошибки при передаче пустого списка"""
    with pytest.raises(ValueError):
        iterator = filter_by_currency([], "USD")
        next(iterator)


# Тестирование функции transaction_descriptions


def test_transaction_descriptions(transactions: list[dict]) -> None:
    """Проверка корректности работы функции"""
    gen = transaction_descriptions(transactions)
    descriptions = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
        "Перевод со счета на счет",
    ]

    for expected_description in descriptions:
        assert next(gen) == expected_description


def test_transaction_descriptions_incorrect(transactions: list[dict]) -> None:
    """Тестирование возникновения ошибки при запросе транзакций, превышающем наличествующие в списке"""
    with pytest.raises(StopIteration):
        iterator = transaction_descriptions(transactions)
        for i in range(10):
            print(next(iterator))


def test_transaction_descriptions_empty_list() -> None:
    """Тестирование возникновения ошибки при передаче пустого списка"""
    iterator = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(iterator)


# Тестирование функции-генератора card_number_generator


def test_card_number_generator() -> None:
    """Проверка корректности работы функции при работе с заданной валютой"""
    gen = card_number_generator(67, 71)
    assert next(gen) == "0000 0000 0000 0067"
    assert next(gen) == "0000 0000 0000 0068"
    assert next(gen) == "0000 0000 0000 0069"
    assert next(gen) == "0000 0000 0000 0070"
    assert next(gen) == "0000 0000 0000 0071"


@pytest.mark.parametrize(
    "start, stop, expected",
    [(1, 1, "0000 0000 0000 0001"), (9999999999999999, 9999999999999999, "9999 9999 9999 9999")],
)
def test_card_number_generator_same(start: int, stop: int, expected: Any) -> None:
    """Тестирование возникновения ошибки при передаче одинакового значения stop и start (максимальные и минимальные)"""
    assert next(card_number_generator(start, stop)) == expected


def test_card_number_generator_incorrect_args() -> None:
    """Тестирование возникновения ошибки при введении значения stop, превышающего значение start"""
    with pytest.raises(StopIteration):
        iterator = card_number_generator(100, 50)
        print(next(iterator))


def test_card_number_generator_incorrect() -> None:
    """Тестирование возникновения ошибки при введении некорректного значения аргумента stop"""
    with pytest.raises(ValueError):
        iterator = card_number_generator(9999999999999999, 10999999999999999)
        print(next(iterator))
