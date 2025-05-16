from src.widget import get_date, mask_account_card
from src.masks import get_mask_account, get_mask_card_number

print(get_mask_card_number(input("Введите номер карты: ")))
print(get_mask_account(input("Введите номер счёта: ")))
print(mask_account_card(input("Введите данные счёта или карты: ")))
print(get_date(input("Введите дату: ")))
