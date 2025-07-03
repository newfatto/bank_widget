import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger("utils_logger")
utils_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
utils_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
utils_handler.setFormatter(utils_formatter)
logger.addHandler(utils_handler)
logger.setLevel(logging.DEBUG)


def transaction_load(file_path: Any) -> list:
    """Функция принимает на вход путь до JSON-файла, и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или список не найден, функция возвращает пустой список"""
    logger.info(f"Принят путь к файлу: {file_path}")
    file_path = Path(file_path)

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            transaction_list = json.load(f)
            if isinstance(transaction_list, list):
                logger.info("JSON-файл преобразован в список словарей")
                return transaction_list
            else:
                logger.info("Список не найден")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning(f"Возникла ошибка {e}")
        return []


if __name__ == "__main__":
    print(
        transaction_load(
            "C:/Users/ekaterina/YandexDisk/Education/Skypro/PycharmProjects/bank_widget/data/operations.json"
        )
    )
