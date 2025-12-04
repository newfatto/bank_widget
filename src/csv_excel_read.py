import os
from typing import Dict, List

import pandas as pd


def csv_to_transaction_list(csv_file: str) -> List[Dict]:
    """
    Читает CSV-файл и возвращает его содержимое в виде списка словарей.
    Args:
        csv_file: Путь к CSV-файлу.
    Returns:
        Список словарей, где каждый словарь представляет строку данных из CSV-файла.
    Raises:
        FileNotFoundError: Если файл не существует.
    """
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"Файл CSV не найден: {csv_file}")

    df = pd.read_csv(csv_file, sep=";")
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col], errors="raise")
        except ValueError:
            pass
    df = df.astype(str)
    transaction_list: List[Dict] = df.to_dict(orient="records")
    return transaction_list


def excel_to_transaction_list(excel_file: str) -> List[Dict]:
    """
    Читает Excel-файл и возвращает его содержимое в виде списка словарей.
    Args:
        excel_file: Путь к Excel-файлу.
    Returns:
        Список словарей, где каждый словарь представляет строку данных из Excel-файла.
    Raises:
        FileNotFoundError: Если файл не существует.
    """
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"Файл Excel не найден: {excel_file}")

    df = pd.read_excel(excel_file)
    transaction_list: List[Dict] = df.to_dict(orient="records")
    return transaction_list
