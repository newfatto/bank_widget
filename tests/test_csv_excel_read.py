from unittest.mock import patch

import pandas as pd
import pytest

from src.csv_excel_read import csv_to_transaction_list, excel_to_transaction_list


def test_csv_to_transaction_list_success() -> None:
    """Тест успешного чтения CSV-файла."""
    expected_result = [{"col1": "1", "col2": "2", "col3": "3"}, {"col1": "a", "col2": "b", "col3": "c"}]

    with patch("os.path.exists", return_value=True), patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({"col1": ["1", "a"], "col2": ["2", "b"], "col3": ["3", "c"]})
        result = csv_to_transaction_list("dummy.csv")
        assert result == expected_result


def test_csv_to_transaction_list_file_not_found() -> None:
    """Тест выброса исключения FileNotFoundError."""
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            csv_to_transaction_list("nonexistent.csv")


def test_csv_to_transaction_list_numeric_conversion() -> None:
    """Тест конвертации числовых значений."""
    expected_result = [{"col1": "1", "col2": "a"}, {"col1": "2", "col2": "b"}]

    with patch("os.path.exists", return_value=True), patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})

        result = csv_to_transaction_list("dummy.csv")
        assert result == expected_result


def test_csv_to_transaction_list_empty_file() -> None:
    """Тест чтения пустого файла."""

    with patch("os.path.exists", return_value=True), patch("pandas.read_csv") as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({"col1": [], "col2": []})

        result = csv_to_transaction_list("dummy.csv")
        assert result == []


def test_excel_to_transaction_list_success() -> None:
    """Тест успешного чтения Excel-файла."""
    expected_result = [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}]

    with patch("os.path.exists", return_value=True), patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
        result = excel_to_transaction_list("dummy.xlsx")
        assert result == expected_result


def test_excel_to_transaction_list_file_not_found() -> None:
    """Тест выброса исключения FileNotFoundError."""
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError):
            excel_to_transaction_list("nonexistent.xlsx")


def test_excel_to_transaction_list_empty_file() -> None:
    """Тест чтения пустого Excel-файла."""

    with patch("os.path.exists", return_value=True), patch("pandas.read_excel") as mock_read_excel:
        mock_read_excel.return_value = pd.DataFrame()  # Пустой DataFrame

        result = excel_to_transaction_list("dummy.xlsx")
        assert result == []  # Пустой список для пустого DataFrame
