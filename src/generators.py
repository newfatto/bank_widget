from typing import Any, Iterator, List


def filter_by_currency(transactions_list: List[dict], currency: str) -> Iterator[Any]:
    """Функция принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно
    выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    if not transactions_list:
        raise ValueError("Список транзакций пуст")

    try:
        filtered_transactions = filter(
            lambda x: x["operationAmount"]["currency"]["name"] == currency, transactions_list
        )
        for transaction in filtered_transactions:
            yield transaction

    except (KeyError, AttributeError):
        raise ValueError("Некорректный формат данных транзакций")


def transaction_descriptions(transactions_list: List[dict]) -> Iterator[Any]:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    if not transactions_list:
        raise ValueError("Список транзакций пуст")

    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[Any]:
    """Функция-генератор принимает стартовое и конечное значение в виде цельных чисел, содержащих от 1 до 16 знаков,
    и генерирует номера карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты."""
    if start >= 1 and stop <= 9999999999999999:
        for i in range(start, stop + 1):
            num = f"{i:0{16}d}"
            yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
    else:
        raise ValueError("Задано некорректное значение")
