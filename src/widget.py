# from . import masks

from src.masks import get_mask_account, get_mask_card_number


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

    for key in types:
        if key in info:
            type = types[key]

    if info[-20:].isdigit():
        return f"{type} {get_mask_account(info[-20:])}"
    elif info[-16:].isdigit():
        return f"{type} {get_mask_card_number(info[-16:])}"
    else:
        return "Вы ввели некорректные данные"


def get_date(date: str) -> str:
    """Функция принимает на вход строку и возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    print(mask_account_card(input("Введите данные счёта или карты: ")))
    print(get_date(input("Введите дату: ")))
    print("Поздравляем, всё успешно!")
