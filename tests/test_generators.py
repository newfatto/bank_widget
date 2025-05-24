import pytest
from src.generators import filter_by_currency

# Проверка работы функции filter_by_currency

def test_filter_by_currency(transactions: list[dict]) -> None:
    """Проверка корректности работы функции при работе с заданной валютой"""
    gen = filter_by_currency(transactions, "USD")
    assert next(gen) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}
    assert next(gen) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
    assert next(gen) == {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}


def test_filter_by_currency_incorrect(transactions) -> None:
    """Тестирование возникновения ошибки при передаче некорректной валюты"""
    with pytest.raises(StopIteration):
        iterator = filter_by_currency(transactions, "TNG")
        next(iterator)


def test_filter_by_currency_empty_list() -> None:
    """Тестирование возникновения ошибки при передаче пустого списка"""
    with pytest.raises(ValueError):
        iterator = filter_by_currency([], "USD")
        next(iterator)

