import telegram_send
from lib.energosbyt import Energosbyt
from lib.ozon import Ozon

if __name__ == "__main__":
    TELEGRAM_TOKEN = '867113998:AAGWKsQE5CGFqtz1AyZI4fFjDOJW16x5kJs'
    CHAT_ID = '-1001431840893'
    path_config = telegram_send.get_config_path()
    with open(path_config, 'w') as f:
        f.write(f'[telegram]\ntoken = {TELEGRAM_TOKEN}\nchat_id = {CHAT_ID}')
    checkers = []
    checkers.append(Energosbyt(base_url="http://enrgsbit.ru/"))
    #checkers.append(Ozon(base_url="https://www.ozon.ru/api/v2"))
    for checker in checkers:
        telegram_send.send(messages=[checker.check()])
