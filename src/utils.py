import json
from pathlib import Path
from typing import Any


def transaction_load(file_path: Any) -> list:
    """Функция принимает на вход путь до JSON-файла, и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или список не найден, функция возвращает пустой список"""
    file_path = Path(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            if isinstance(transaction_list, list):
                return transaction_list
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


if __name__ == "__main__":
    print(
        transaction_load(
            "C:/Users/ekaterina/YandexDisk/Education/Skypro/PycharmProjects/bank_widget/data/operations.json"
        )
    )
