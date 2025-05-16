from typing import Dict, List


def filter_by_state(dict_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает новый список, содержащий словари, где ключ state соответствует указанному значению."""
    return [d for d in dict_list if d.get("state") == state]


def sort_by_date(dict_list: List[Dict], is_reverse: bool = True) -> List[Dict]:
    """Функция принимает список словарей и параметр сортировки и возвращает список, отсортированный по дате."""
    return sorted(dict_list, key=lambda x: x.get("date", float("inf")), reverse=is_reverse)


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
