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

    account_type = 0

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
        raise TypeError ("Вы ввели некорректные данные")


def get_date(date: str) -> str:
    """Функция принимает на вход строку и возвращает дату в формате ДД.ММ.ГГГГ"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    print(mask_account_card("Счет 764"))
    print(mask_account_card(input("Введите данные счёта или карты: ")))
    print(get_date(input("Введите дату: ")))
    print("Поздравляем, всё успешно!")
