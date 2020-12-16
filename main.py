import requests
import telegram_send



class Checker:
    def __init__(self):
        pass

    def check_energosbyt(self):
        data = {"licnum": 91019214}
        response = requests.post(\
            "http://enrgsbit.ru/local/components/form/saratov.zadolzhennost/ajax.php", data=data)
        if response.status_code == 200:
            in_list = response.json()['html'].split(">")
            in_list.pop(7)
            in_list.pop(3)
            in_list.pop(0)
            out_list = []
            for item in in_list:
                out_list.append(item.replace(item[item.find("<"):len(item)],""))
            substr1 = "".join(out_list[0:2])
            substr2 = "".join(out_list[2:5])
            return f"{substr1} {substr2}"

if __name__ == "__main__":
    TELEGRAM_TOKEN = '867113998:AAGWKsQE5CGFqtz1AyZI4fFjDOJW16x5kJs'
    CHAT_ID = '-1001431840893'
    path_config = telegram_send.get_config_path()
    with open(path_config, 'w') as f:
        f.write(f'[telegram]\ntoken = {TELEGRAM_TOKEN}\nchat_id = {CHAT_ID}')
    checker = Checker()
    telegram_send.send(messages=["Энергосбыт (тепло и горячая вода).\n" +\
        checker.check_energosbyt()])
