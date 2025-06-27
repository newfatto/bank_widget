from typing import Any

import pytest

from src.decorators import log

# Тестирование работы функции при введённом имени файла (сохранение логов в файл)


@pytest.mark.parametrize(
    "test_x , test_y, expected", [(1, 2, 3), ("раз", "два", "раздва"), ([1, 2], [3, 4], [1, 2, 3, 4])]
)
def test_log(test_x: Any, test_y: Any, expected: Any) -> None:
    """Тестирование работы функции при корректных значениях аргументов функции"""

    @log(filename="mylog.txt")
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    result = my_function(test_x, test_y)
    assert result == expected


def test_log_error() -> None:
    """Тестирование работы функции при некорректных значениях аргументов функции"""
    with pytest.raises(Exception):

        @log(filename="mylog.txt")
        def my_function(x: Any, y: Any) -> Any:
            return x + y

        my_function(1, "два")


# Тестирование работы функции при отсутствующем имени файла (вывод логов в консоль)


def test_log_no_path(capsys: pytest.CaptureFixture) -> None:
    """Тестирование работы функции при корректных значениях аргументов функции"""

    @log()
    def my_function(x: Any, y: Any) -> Any:
        return x + y

    result = my_function(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert captured.out == "my_function ok\n"


def test_log_no_path_error(capsys: pytest.CaptureFixture) -> None:
    """Тестирование работы функции при некорректных значениях аргументов функции"""
    with pytest.raises(Exception):

        @log()
        def my_function(x: Any, y: Any) -> Any:
            return x + y

        my_function([1, 3, 6], "десять")
        captured = capsys.readouterr()
        assert captured.out == "my_function Error: <class 'TypeError'> Inputs: (([1, 3, 6], 'десять'), {})\n"
