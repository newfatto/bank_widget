def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    ready_card_number = "".join(i for i in card_number if i.isdigit())
    if len(ready_card_number) < 13 or len(ready_card_number) > 20:
        raise TypeError("Вы ввели некорректный номер карты")
    else:
        return f"{str(ready_card_number)[0:4]} {str(ready_card_number)[4:6]}** **** {str(ready_card_number)[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    ready_account_number = "".join(i for i in account_number if i.isdigit())
    if len(ready_account_number) < 20 or len(ready_account_number) > 35:
        raise TypeError("Вы ввели некорректный номер счёта")
    else:
        return f"** {str(ready_account_number)[-4:]}"
