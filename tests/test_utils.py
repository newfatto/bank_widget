import json
from unittest.mock import mock_open, patch

from src.utils import transaction_load


def test_transaction_load_correct_json_mocked() -> None:
    """Тестирование функции transaction_load при введении корректного пути к json файлу"""
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": -50}]
    mock_json_data = json.dumps(mock_data)
    mock_file = mock_open(read_data=mock_json_data)

    with patch("builtins.open", mock_file):  # Патчим встроенную функцию open
        result = transaction_load("dummy_path.json")
        assert result == mock_data


def test_transaction_load_incorrect_json_mocked() -> None:
    """Тестирование функции transaction_load при ссылке на некорректный json файл"""
    mock_data = "invalid json"
    mock_file = mock_open(read_data=mock_data)

    with patch("builtins.open", mock_file):
        result = transaction_load("dummy_path.json")
        assert result == []


def test_transaction_load_empty_file_mocked() -> None:
    """Тестирование функции transaction_load при ссылке на пустой json файл"""
    mock_file = mock_open(read_data="")

    with patch("builtins.open", mock_file):
        result = transaction_load("dummy_path.json")
        assert result == []


def test_transaction_load_file_not_found_mocked() -> None:
    """Тестирование функции transaction_load в случае, когда файл не найден"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = transaction_load("dummy_path.json")
        assert result == []
