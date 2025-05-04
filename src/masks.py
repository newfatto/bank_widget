# Номер карты 7000792289606361
# Номер счёта 73654108430135874305


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"** {str(account_number)[-4:]}"
