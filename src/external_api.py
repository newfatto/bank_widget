import json
import os

import requests
from dotenv import load_dotenv

from src.utils import transaction_load

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"
API_HEADERS = {"apikey": API_KEY}
MAX_RETRIES = 3


def convert_transaction_to_rubles(transaction: dict) -> float | None:
    """Конвертирует сумму транзакции в рубли.
    Args:
        transaction: Словарь с данными о транзакции.
    Returns:
        Сумма транзакции в рублях (float), или None в случае ошибки."""
    if not API_KEY:
        print("Ошибка: API_KEY не установлен в переменных окружения.")
        return None

    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        if currency == "RUB":
            return float(amount)

        for i in range(MAX_RETRIES):
            try:
                url = f"{API_URL}?to=RUB&from={currency}&amount={amount}"
                response = requests.get(url, headers=API_HEADERS)
                response.raise_for_status()  # Возбудить ошибку HTTPError для неудачных запросов (после 3 попытки)
                data = response.json()
                result = float(data["result"])
                return result
            except requests.exceptions.RequestException as e:
                print(f"Попытка {i + 1}/{MAX_RETRIES}: Ошибка при запросе к API: {e}")
                if i == MAX_RETRIES - 1:
                    print("Превышено максимальное количество попыток.")
                    return None
                return None
            except json.JSONDecodeError as e:
                print(f"Ошибка декодирования JSON: {e}")
                return None
            except KeyError as e:
                print(f"Ошибка: Отсутствует ключ в ответе API: {e}")
                return None
        return None
    except (KeyError, ValueError) as e:
        print(f"Ошибка: Неверный формат транзакции: {e}")
        return None


if __name__ == "__main__":
    trans = transaction_load(
        "C:/Users/ekaterina/YandexDisk/Education/Skypro/PycharmProjects/bank_widget/data/operations.json"
    )[3]
    print(convert_transaction_to_rubles(trans))
