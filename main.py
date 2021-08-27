import telegram_send
from lib.energosbyt import Energosbyt
from lib.ozon import Ozon

if __name__ == "__main__":
    checkers = []
    checkers.append(Energosbyt(base_url="http://enrgsbit.ru/"))
    #checkers.append(Ozon(base_url="https://www.ozon.ru/api/v2"))
    for checker in checkers:
        telegram_send.send(conf="./telegram-send.conf", messages=[checker.check()])
