from collections import defaultdict
from typing import Any, Dict, List, Optional

from src.csv_excel_read import csv_to_transaction_list, excel_to_transaction_list
from src.generators import filter_by_currency
from src.processing import filter_by_state, filter_transactions_by_description, sort_by_date
from src.utils import transaction_load
from src.widget import get_date, mask_account_card


def main() -> None:
    user_file: List[Dict[str, Any]] = []
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n")
    while True:
        user_input = input(
            "Выберите необходимый пункт меню: \n"
            "1. Получить информацию о транзакциях из JSON-файла \n"
            "2. Получить информацию о транзакциях из CSV-файла \n"
            "3. Получить информацию о транзакциях из XLSX-файла \n"
            "Введите 1, 2 или 3: "
        )
        if user_input in ("1", "2", "3"):
            break
        else:
            print("Вы ввели некорректные данные")

    if user_input == "1":
        print("Для обработки выбран JSON-файл")
        raw_file = transaction_load("data/operations.json")
        user_file = []
        for transaction in raw_file:
            transaction_dict: Dict[str, Optional[Any]] = defaultdict(lambda: None)
            transaction_dict["id"] = transaction.get("id")
            transaction_dict["state"] = transaction.get("state")
            transaction_dict["date"] = transaction.get("date")

            operation_amount = transaction.get("operationAmount", {})
            transaction_dict["amount"] = operation_amount.get("amount") if operation_amount else None

            currency = operation_amount.get("currency", {}) if operation_amount else {}
            transaction_dict["currency_name"] = currency.get("name") if currency else None
            transaction_dict["currency_code"] = currency.get("code") if currency else None

            transaction_dict["from"] = transaction.get("from")
            transaction_dict["to"] = transaction.get("to")
            transaction_dict["description"] = transaction.get("description")
            user_file.append(dict(transaction_dict))

    elif user_input == "2":
        print("Для обработки выбран CSV-файл")
        user_file = csv_to_transaction_list("data/transactions.csv")

    elif user_input == "3":
        print("Для обработки выбран XLSX-файл")
        user_file = excel_to_transaction_list("data/transactions_excel.xlsx")

    while True:
        user_state = input(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING: "
        ).upper()
        if user_state in ("EXECUTED", "CANCELED", "PENDING"):
            break
        else:
            print(f"Статус {user_state} недоступен.")

    result = filter_by_state(user_file, user_state)

    print(f"Операции отфильтрованы по статусу {user_state}")

    while True:
        user_sort_by_date = input("Отсортировать операции по дате?\n" 'Введите "Да" или "Нет": ').lower()
        if user_sort_by_date == "да":
            while True:
                user_sort_by_date_up_or_down = input(
                    "Каким образом отсортировать?\n" "Введите 'по возрастанию' или 'по убыванию': "
                ).lower()
                if user_sort_by_date_up_or_down == "по возрастанию":
                    result = sort_by_date(result, False)
                    print("Данные отсортированы по возрастанию даты")
                    break
                elif user_sort_by_date_up_or_down == "по убыванию":
                    result = sort_by_date(result, True)
                    print("Данные отсортированы по убыванию даты")
                    break
                else:
                    print("Вы ввели некорректные данные")
            break
        elif user_sort_by_date == "нет":
            break
        else:
            print("Вы ввели некорректные данные.")

    while True:
        user_filter_rub = input("Выводить только рублёвые транзакции?\n" 'Введите "Да" или "Нет": ').lower()
        if user_filter_rub == "да":
            result = list(filter_by_currency(result, "RUB")) + list(filter_by_currency(result, "руб."))
            break
        elif user_filter_rub == "нет":
            break
        else:
            print("Вы ввели некорректные данные.")

    while True:
        user_filter_word = input(
            "Отфильтровать список транзакций по определенному слову?\n" 'Введите "Да" или "Нет": '
        ).lower()

        if user_filter_word == "да":
            user_word = str(input("Впишите слово для фильтрации: "))
            result = filter_transactions_by_description(result, user_word)
            break

        elif user_filter_word == "нет":
            break
        else:
            print("Вы ввели некорректные данные.")
    print("Распечатываю итоговый список транзакций...")

    if len(result) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    else:
        print(f"Всего банковских операций в выборке: {len(result)}\n")
        for transaction in result:
            print(
                f"{get_date(transaction['date'])} {transaction['description']}\n"
                f"{mask_account_card(transaction['to'])} "
                f"Сумма: {transaction['amount']}\n \n"
            )

    return None


main()
