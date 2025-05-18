import locale
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

locale.setlocale(locale.LC_ALL, "ru_RU")


def mask_account_card(info: str) -> str:
    """Функция, принимающая информацию о счетах и картах и возвращающая их маску"""
    types = {
        "Maestro": "Maestro",
        "Счет": "Счет",
        "MasterCard": "MasterCard",
        "Visa Classic": "Visa Classic",
        "Visa Platinum": "Visa Platinum",
        "Visa Gold": "Visa Gold",
    }

    account_type = ""

    for key in types:
        if key in info:
            account_type = types[key]

    if account_type is None:
        raise ValueError("Не удалось определить тип счёта")

    ready_info = "".join(i for i in info if i.isdigit())

    if account_type == "Счет":
        return f"{account_type} {get_mask_account(ready_info)[-4::]}"
    elif ready_info[-13:].isdigit():
        return f"{account_type} {get_mask_card_number(ready_info)}"
    else:
        raise TypeError("Вы ввели некорректные данные")


def get_date(date_string: str) -> str:
    """Функция принимает на вход строку и возвращает дату в формате ДД.ММ.ГГГГ"""
    formats = [
        "%Y-%m-%d",  # ISO 8601 формат (2024-03-11)
        "%d/%m/%Y",  # Европейский формат (11/03/2024)
        "%m/%d/%Y",  # Американский формат (03/11/2024)
        "%Y/%m/%d",  # Японский формат (2024/03/11)
        "%d %B %Y",  # С полным названием месяца (11 марта 2024)
        "%d %b %Y",  # С сокращенным названием месяца (11 мар 2024)
        "%Y-%m-%dT%H:%M:%S",  # ISO с временем (2024-03-11T02:26:18)
        "%Y-%m-%d %H:%M:%S",  # ISO с временем (2024-03-11 02:26:18)
        "%d.%m.%Y",  # Уже нужный формат (11.03.2024)
    ]

    for x in formats:
        try:
            date = datetime.strptime(date_string, x)
            return date.strftime("%d.%m.%Y")
        except ValueError:
            continue

    raise ValueError(f"Не удалось определить формат даты: {date_string}")
