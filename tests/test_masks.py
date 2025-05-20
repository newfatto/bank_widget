import pytest

from src.masks import get_mask_account, get_mask_card_number

# Тестирование функции get_mask_card_number()


def test_get_mask_card_number() -> None:
    """Проверка правильности маскировки номера карты"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_get_mask_card_number_with_spases() -> None:
    """Проверка правильности маскировки при введении номера карты с пробелами"""
    assert get_mask_card_number("7000 7922 8960 6361") == "7000 79** **** 6361"


def test_get_mask_card_number_long_number() -> None:
    """Проверка правильности маскировки при введении длинного номера (но короче 20 символов)"""
    assert get_mask_card_number("7000792289606369830") == "7000 79** **** 9830"


def test_get_mask_card_number_empty() -> None:
    """Проверка отработки ошибки при введении пустой строки"""
    with pytest.raises(TypeError):
        get_mask_card_number("")


def test_get_mask_card_number_too_much() -> None:
    """Проверка отработки ошибки при введении лишком длинного номера (более 20 символов)"""
    with pytest.raises(TypeError):
        get_mask_card_number("3487547998372382782748398237")


# Тестирование функции get_mask_account()


def test_get_mask_account() -> None:
    """Проверка правильности маскировки номера карты"""
    assert get_mask_account("73654108430135874305") == "** 4305"


def test_get_mask_account_with_spases() -> None:
    """Проверка правильности маскировки при введении номера карты с пробелами"""
    assert get_mask_account("7365 4108 4301 3587 4305") == "** 4305"


def test_get_mask_account_long_number() -> None:
    """Проверка правильности маскировки при введении номера счёта в международном формате"""
    assert get_mask_account("RU12345678901234567890") == "** 7890"


def test_get_mask_account_empty() -> None:
    """Проверка отработки ошибки при введении пустой строки"""
    with pytest.raises(TypeError):
        get_mask_account("")


def test_get_mask_account_too_much() -> None:
    """Проверка отработки ошибки при введении лишком длинного номера (более 20 символов)"""
    with pytest.raises(TypeError):
        get_mask_account("3487547998355678972382782748878398237")
