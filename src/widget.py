import locale
from typing import Any, Optional

from dateutil import parser

from src.masks import get_mask_account, get_mask_card_number

locale.setlocale(locale.LC_ALL, "ru_RU")


def mask_account_card(info: str) -> Optional[str]:
    """Функция, принимающая информацию о счетах и картах и возвращающая их маску"""
    types = {
        "Maestro": "Maestro",
        "Счет": "Счет",
        "MasterCard": "MasterCard",
        "Masterсard": "MasterCard",
        "Visa Classic": "Visa Classic",
        "Visa Platinum": "Visa Platinum",
        "Visa Gold": "Visa Gold",
        "Visa": "Visa",
        "American Express": "American Express",
        "Discover": "Discover",
    }

    account_type = ""
    for key in types:
        if key in info:
            account_type = types[key]
            break

    ready_info = "".join(i for i in info if i.isdigit())

    if account_type == "Счет":
        try:
            return f"{account_type} {get_mask_account(ready_info)}"
        except TypeError:
            raise TypeError
    elif account_type:
        try:
            return f"{account_type} {get_mask_card_number(ready_info)}"
        except TypeError:
            raise TypeError
    else:
        return None


def get_date(date_string: str) -> str | Any:
    """Функция принимает на вход строку и возвращает дату в формате ГГГГ-ММ-ДД"""
    try:
        date = parser.parse(date_string)
        return date.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Не удалось определить формат даты: {date_string}")
