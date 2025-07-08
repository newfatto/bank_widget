from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.csv_excel_read import csv_to_transaction_list, excel_to_transaction_list


@patch("os.path.exists")
@patch("pandas.read_csv")
def test_csv_to_transaction_list_success(mock_read_csv: MagicMock, mock_exists: MagicMock) -> None:
    """Тест успешного чтения CSV файла."""
    mock_exists.return_value = True
    mock_read_csv.return_value = pd.DataFrame([{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}])

    assert csv_to_transaction_list("test.csv") == [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}]
    mock_read_csv.assert_called_once_with("test.csv")
    mock_exists.assert_called_once_with("test.csv")


@patch("os.path.exists")
def test_csv_to_transaction_list_file_not_found(mock_exists: MagicMock) -> None:
    """Тест, когда CSV файл не найден."""
    mock_exists.return_value = False
    with pytest.raises(FileNotFoundError) as e:
        csv_to_transaction_list("nonexistent.csv")
    assert str(e.value) == "Файл CSV не найден: nonexistent.csv"
    mock_exists.assert_called_once_with("nonexistent.csv")


@patch("os.path.exists")
@patch("pandas.read_excel")
def test_excel_to_transaction_list_success(mock_read_excel: MagicMock, mock_exists: MagicMock) -> None:
    """Тест успешного чтения Excel файла."""
    mock_exists.return_value = True
    mock_read_excel.return_value = pd.DataFrame([{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}])

    assert excel_to_transaction_list("test.xlsx") == [{"col1": 1, "col2": "a"}, {"col1": 2, "col2": "b"}]
    mock_read_excel.assert_called_once_with("test.xlsx")
    mock_exists.assert_called_once_with("test.xlsx")


@patch("os.path.exists")
def test_excel_to_transaction_list_file_not_found(mock_exists: MagicMock) -> None:
    """Тест, когда Excel файл не найден."""
    mock_exists.return_value = False
    with pytest.raises(FileNotFoundError) as e:
        excel_to_transaction_list("nonexistent.csv")
    assert str(e.value) == "Файл Excel не найден: nonexistent.csv"
    mock_exists.assert_called_once_with("nonexistent.csv")
