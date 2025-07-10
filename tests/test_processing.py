from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, filter_transactions_by_description, process_bank_operations, sort_by_date

# Тестирование функции filter_by_state()


@pytest.fixture
def mylist() -> list[dict]:
    """Фикстура, предоставляющая список словарей."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
        {"id": 123456789, "date": "2024-01-01T00:00:00"},  # Без "state"
    ]


def test_filter_by_state_canceled(mylist: List[Dict]) -> None:
    """Тестирование фильтрации списка словарей по заданному статусу state"""
    assert filter_by_state(mylist, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
    ]


def test_filter_by_state_default(mylist: List[Dict]) -> None:
    """Тестирование фильтрации списка словарей при отсутствии параметра state (используется значение по умолчанию)"""
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
def test_filter_by_state_parametrize(mylist: List[Dict], state: str, expected: List[Dict]) -> None:
    """Тестирование при различных параметрах state (используем parametrize)"""
    assert filter_by_state(mylist, state) == expected


def test_filter_by_state_incorrect_state(mylist: List[Dict]) -> None:
    """Тестирование, что не возникает ошибки при некорректном параметре state (должен возвращаться пустой список)"""
    assert filter_by_state(mylist, "ЗНАЧЕНИЕ") == []


def test_filter_by_state_empty_list() -> None:
    """Тестирование возврата None при передаче пустого списка"""
    assert filter_by_state([], "EXECUTED") == []


def test_filter_by_state_missing_state(mylist: List[Dict]) -> None:
    """Тестирование, что словари без ключа 'state' не включаются в результат"""
    assert filter_by_state(mylist, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
    ]
    assert filter_by_state(mylist) == [  # Тест default
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58"},
    ]


# Тестирование функции sort_by_date()


@pytest.fixture
def my_list() -> list[dict]:
    """Фикстура для списка словарей для тестов."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
    ]


def test_sort_by_date(my_list: list[dict]) -> None:
    """Проверка функции сортировки по дате (без определения параметра - убывание)"""
    expected = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
    ]
    assert sort_by_date(my_list) == expected


def test_sort_by_date_reverse(my_list: list[dict]) -> None:
    """Проверка функции сортировки по дате (по возрастанию)"""
    expected = [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03"},
    ]
    assert sort_by_date(my_list, False) == expected


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


# Тестирование функции filter_transactions_by_description


def test_filter_transactions_empty_list() -> None:
    """Тест для пустого списка транзакций."""
    assert filter_transactions_by_description([], "test") == []


def test_filter_transactions_no_match() -> None:
    """Тест, когда ни одна транзакция не соответствует критерию поиска."""
    transactions = [
        {"id": 1, "description": "Transaction A"},
        {"id": 2, "description": "Transaction B"},
    ]
    assert filter_transactions_by_description(transactions, "nonexistent") == []


def test_filter_transactions_single_match() -> None:
    """Тест, когда только одна транзакция соответствует критерию поиска."""
    transactions = [
        {"id": 1, "description": "Transaction A"},
        {"id": 2, "description": "Matching Transaction"},
        {"id": 3, "description": "Transaction C"},
    ]
    expected = [{"id": 2, "description": "Matching Transaction"}]
    assert filter_transactions_by_description(transactions, "Matching") == expected


def test_filter_transactions_multiple_matches() -> None:
    """Тест, когда несколько транзакций соответствуют критерию поиска."""
    transactions = [
        {"id": 1, "description": "Matching Transaction 1"},
        {"id": 2, "description": "Matching Transaction 2"},
        {"id": 3, "description": "Transaction C"},
    ]
    expected = [
        {"id": 1, "description": "Matching Transaction 1"},
        {"id": 2, "description": "Matching Transaction 2"},
    ]
    assert filter_transactions_by_description(transactions, "Matching") == expected


# Тестирование функции process_bank_operations


def test_process_bank_operations_basic() -> None:
    """
    Базовый тест с несколькими категориями и транзакциями
    """
    transactions = [
        {"description": "Продукты", "amount": 1000},
        {"description": "Транспорт", "amount": 500},
        {"description": "Продукты", "amount": 800},
        {"description": "Развлечения", "amount": 2000},
    ]
    categories = ["Продукты", "Транспорт", "Развлечения"]

    expected = {"Продукты": 2, "Транспорт": 1, "Развлечения": 1}

    result = process_bank_operations(transactions, categories)
    assert result == expected


def test_process_bank_operations_empty_transactions() -> None:
    """
    Тест с пустым списком транзакций
    """
    transactions: List[Dict[str, Any]] = []
    categories = ["Продукты", "Транспорт"]

    expected: Dict[str, int] = {}

    result = process_bank_operations(transactions, categories)
    assert result == expected


def test_process_bank_operations_no_matching_transactions() -> None:
    """
    Тест когда нет совпадений с категориями
    """
    transactions = [{"description": "Продукты", "amount": 1000}, {"description": "Транспорт", "amount": 500}]
    categories = ["Развлечения", "Медицина"]

    expected: Dict[str, int] = {}

    result = process_bank_operations(transactions, categories)
    assert result == expected


def test_process_bank_operations_single_category() -> None:
    """
    Тест с одной категорией
    """
    transactions = [
        {"description": "Продукты", "amount": 1000},
        {"description": "Продукты", "amount": 800},
        {"description": "Продукты", "amount": 500},
    ]
    categories = ["Продукты"]

    expected = {"Продукты": 3}

    result = process_bank_operations(transactions, categories)
    assert result == expected


def test_process_bank_operations_invalid_transactions_type() -> None:
    """
    Тест с некорректным типом transactions
    """
    try:
        process_bank_operations("не список", ["Продукты"])
    except TypeError as e:
        assert str(e) == "transactions должен быть списком."


def test_process_bank_operations_invalid_categories_type() -> None:
    """
    Тест с некорректным типом categories
    """
    try:
        process_bank_operations([{"description": "Продукты"}], "не список")
    except TypeError as e:
        assert str(e) == "categories должен быть списком."


def test_process_bank_operations_mixed_categories() -> None:
    """
    Тест с разными категориями и разными количествами
    """
    transactions = [
        {"description": "Продукты", "amount": 1000},
        {"description": "Транспорт", "amount": 500},
        {"description": "Продукты", "amount": 800},
        {"description": "Развлечения", "amount": 2000},
        {"description": "Транспорт", "amount": 300},
        {"description": "Транспорт", "amount": 400},
    ]
    categories = ["Продукты", "Транспорт", "Развлечения"]

    expected = {"Продукты": 2, "Транспорт": 3, "Развлечения": 1}

    result = process_bank_operations(transactions, categories)
    assert result == expected
