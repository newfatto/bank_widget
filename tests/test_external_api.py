from unittest.mock import Mock, patch


from src.external_api import convert_transaction_to_rubles


def test_convert_transaction_to_rubles_rub() -> None:
    """Тестирование функции convert_transaction_to_rubles с корректными значениями (в рублях, без конвертации)"""
    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "RUB"}}}
    assert convert_transaction_to_rubles(transaction) == 100.00


@patch("src.external_api.requests.get")
def test_convert_transaction_to_rubles_usd(mock_get: Mock) -> None:
    """Тестирование функции convert_transaction_to_rubles с корректными значениями (в долларах, с конвертацией)"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 7500.00}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    result = convert_transaction_to_rubles(transaction)
    assert result == 7500.00


@patch("src.external_api.requests.get")
def test_convert_transaction_to_rubles_api_error(mock_get: Mock) -> None:
    """Тестирование функции convert_transaction_to_rubles с симуляцией ошибки API"""
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {"error": "Internal Server Error"}
    mock_get.return_value = mock_response

    transaction = {"operationAmount": {"amount": "100.00", "currency": {"code": "USD"}}}
    assert convert_transaction_to_rubles(transaction) is None


def test_convert_transaction_to_rubles_missing_key() -> None:
    """Тестирование функции convert_transaction_to_rubles с отсутствующей валютой"""
    transaction = {"operationAmount": {"amount": "100.00"}}
    assert convert_transaction_to_rubles(transaction) is None


def test_convert_transaction_to_rubles_invalid_amount() -> None:
    """Тестирование функции convert_transaction_to_rubles с некорректными значениями суммы операции"""
    transaction = {"operationAmount": {"amount": "abc", "currency": {"code": "USD"}}}
    result = convert_transaction_to_rubles(transaction)
    assert result is None
