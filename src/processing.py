from datetime import datetime
from typing import Dict, List

from src.widget import get_date


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> list[dict] | None:
    """Функция возвращает новый список, содержащий словари, где ключ state соответствует указанному значению."""
    for x in dict_list:
        if state == x["state"]:
            return [d for d in dict_list if d.get("state") == state]
        else:
            continue
    raise ValueError("Ошибка ввода данных")


def sort_by_date(dict_list: List[Dict], is_reverse: bool = True) -> list[dict] | None:
    """Функция принимает список словарей и параметр сортировки и возвращает список, отсортированный по дате."""
    if not dict_list:  # Добавляем проверку на пустой список
        raise ValueError("Список словарей пуст")

    for x in dict_list:
        if "date" not in x:
            raise KeyError("Ошибка ввода данных")
        else:
            ready_date = get_date(x["date"])
            x["date"] = ready_date
    return sorted(
        dict_list, key=lambda x: datetime.strptime(x.get("date", "9999-12-31"), "%d.%m.%Y"), reverse=is_reverse
    )
