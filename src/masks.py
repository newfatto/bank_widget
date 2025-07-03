import logging

logger = logging.getLogger('masks_logger')
masks_handler = logging.FileHandler('logs/masks.log', mode='w', encoding='utf-8')
masks_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s: %(message)s')
masks_handler.setFormatter(masks_formatter)
logger.addHandler(masks_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.info(f'Введён номер карты: {card_number}')
    ready_card_number = "".join(i for i in card_number if i.isdigit())
    if len(ready_card_number) < 13 or len(ready_card_number) > 20:
        logger.error('Некорректный номер карты')
        raise TypeError("Вы ввели некорректный номер карты")
    else:
        logger.info(f'Номер карты форматируется')
        return f"{str(ready_card_number)[0:4]} {str(ready_card_number)[4:6]}** **** {str(ready_card_number)[-4:]}"



def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.info(f'Введён номер счёта: {account_number}')
    ready_account_number = "".join(i for i in account_number if i.isdigit())
    if len(ready_account_number) < 20 or len(ready_account_number) > 35:
        logger.error('Введён некорректный номер счёта')
        raise TypeError("Вы ввели некорректный номер счёта")
    else:
        logger.info(f'Номер счёта форматируется')
        return f"** {str(ready_account_number)[-4:]}"
