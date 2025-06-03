from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Any:
    """Декоратор принимает в качестве аргумента имя файла, в который будут записываться логи
    и фиксирует в этом файле результат выполнения функции. В случае успешного выполнения записывает
    в логи имя функции и 'ок', в случае неуспешного - имя функции, тип ошибки и аргументы функции.
    Если имя файла не указано - результат работы выводится в консоль"""

    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | None:
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} Error: {type(e)} Inputs: {args, kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e)}. Inputs: {args, kwargs}")
                raise

        return wrapper

    return decorator
