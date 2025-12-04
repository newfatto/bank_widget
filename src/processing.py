import re
from collections import Counter
from typing import Dict, List

from src.widget import get_date


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список, содержащий словари, где ключ state соответствует указанному значению."""
    filtered_list = [d for d in dict_list if "state" in d and d["state"] == state]
    return filtered_list


def sort_by_date(dict_list: List[Dict], is_reverse: bool = True) -> list[dict]:
    """Функция принимает список словарей и параметр сортировки и возвращает список, отсортированный по дате."""
    if not dict_list:  # Добавляем проверку на пустой список
        raise ValueError("Список словарей пуст")

    dict_list_copy = [d.copy() for d in dict_list]

    for transaction in dict_list_copy:
        if "date" not in transaction:
            raise KeyError("Ошибка ввода данных")
        else:
            transaction["date"] = get_date(transaction["date"])
    return sorted(dict_list_copy, key=lambda x: (x["date"], x["id"]), reverse=is_reverse)


def filter_transactions_by_description(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Функция принимает на вход список словарей с данными о банковских операциях и строку поиска, и возвращает
    список словарей, у которых в описании есть данная строка
    """
    filtered_transactions = []
    try:
        pattern = re.compile(search_string, re.IGNORECASE)
        for transaction in transactions:
            if isinstance(transaction.get("description"), str):
                if pattern.search(transaction["description"]):
                    filtered_transactions.append(transaction)
    except KeyError as e:
        print(f"Ошибка: KeyError: {e}.")
    except TypeError as e:
        print(f"Ошибка: TypeError: {e}.")
    except re.error as e:
        print(f"Ошибка: Regular Expression Error: {e}.")
    except Exception as e:
        print(f"Ошибка: {e}.")

    return filtered_transactions


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """
    Анализирует список банковских операций и возвращает словарь с количеством операций по категориям.

    Args:
        transactions:Список словарей с данными о банковских операциях.
        Каждый словарь должен содержать ключ 'description'.
        categories: Список категорий для подсчета.

    Returns:
        Словарь, где ключи - названия категорий, а значения - количество операций в каждой категории.

    Raises:
        TypeError: Если `transactions` не является списком или `categories` не является списком.
        ValueError:Если `transactions` содержит элементы, не являющиеся словарями, или если в словарях отсутствует
        ключ 'description'.
    """
    if not isinstance(transactions, list):
        raise TypeError("transactions должен быть списком.")
    if not isinstance(categories, list):
        raise TypeError("categories должен быть списком.")
    description_list = []
    for category in categories:
        description_list.extend(
            [transaction["description"] for transaction in transactions if category == transaction["description"]]
        )
    print(description_list)
    counted = Counter(description_list)
    return dict(counted)
