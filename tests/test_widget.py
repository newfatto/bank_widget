import pytest

from src.widget import get_date, mask_account_card

# Тестирование функции mask_account_card()


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет 9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35 3830 3347 4447 8955 60", "Счет 5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999 4142 2842 6353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет 4305"),
        ("Счет RU12345678901234567890", "Счет 7890"),
    ],
)
def test_mask_account_card(info: str, expected: str) -> None:
    """Проверка правильности маскировки при введении данных в разных форматах (с пробелами и буквами)"""
    assert mask_account_card(info) == expected


def test_mask_account_card_incorrect_account() -> None:
    """Проверка возникновения ошибки при введении некорректного номера счёта"""
    with pytest.raises(TypeError):
        mask_account_card("Счет 764")


def test_mask_account_card_empty() -> None:
    """Проверка отработки ошибки при введении пустой строки"""
    with pytest.raises(ValueError):
        mask_account_card("")


def test_mask_account_card_too_much() -> None:
    """Проверка отработки ошибки при введении лишком длинного номера (более 20 символов)"""
    with pytest.raises(TypeError):
        mask_account_card("Счет 3487547998355678972382782748878398237")


def test_mask_account_card_no_account_type() -> None:
    """Проверка отработки ошибки при введении номера без указания типа счёта"""
    with pytest.raises(ValueError):
        mask_account_card("348754799835567897")


# Тестирование функции get_date()


@pytest.mark.parametrize(
    "date, expected",
    [
        ("2024-03-11", "11.03.2024"),
        ("11/03/2024", "11.03.2024"),
        ("03/11/2024", "03.11.2024"),
        ("2024/03/11", "11.03.2024"),
        ("11 март 2024", "11.03.2024"),
        ("11 мар 2024", "11.03.2024"),
        ("2024-03-11T02:26:18", "11.03.2024"),
        ("11.03.2024", "11.03.2024"),
        ("2024-03-11", "11.03.2024"),
    ],
)
def test_get_date(date: str, expected: str) -> None:
    """Проверка правильности преобразования даты с введением даты в различных форматах"""
    assert get_date(date) == expected


def test_get_date_empy() -> None:
    """Проверка возникновения ошибки при введении пустой строки"""
    with pytest.raises(ValueError):
        get_date("")


def test_get_date_incorrect() -> None:
    """Проверка возникновения ошибки при введении некорректной строки"""
    with pytest.raises(ValueError):
        get_date("Одиннадцатое марта две тысячи двадцать четвёртого года")
