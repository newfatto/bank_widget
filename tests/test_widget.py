import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("info, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                            ("Счет 64686473678894779589", "Счет 9589"),
                                            ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                            ("Счет 35 3830 3347 4447 8955 60", "Счет 5560"),
                                            ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                            ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                            ("Visa Gold 5999 4142 2842 6353", "Visa Gold 5999 41** **** 6353"),
                                            ("Счет 73654108430135874305", "Счет 4305"),
                                            ("Счет RU12345678901234567890", "Счет 7890")
                                            ])
def test_mask_account_card(info,expected):
    """Проверка правильности маскировки при введении данных в разных форматах (с пробелами и буквами)"""
    assert mask_account_card(info) == expected


def test_mask_account_card_incorrect_account():
    """Проверка возникновения ошибки при введении некорректного номера счёта"""
    with pytest.raises(TypeError):
        mask_account_card("Счет 764")


def test_mask_account_card_empty():
    """Проверка отработки ошибки при введении пустой строки"""
    with pytest.raises(TypeError):
        mask_account_card("")


def test_mask_account_card_too_much():
    """Проверка отработки ошибки при введении лишком длинного номера (более 20 символов)"""
    with pytest.raises(TypeError):
        mask_account_card("3487547998355678972382782748878398237")
