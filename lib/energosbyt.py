import requests
from lib.provider import Provider

class Energosbyt(Provider):

    def check(self):
        data = {"licnum": 91019214}
        response = requests.post(\
            f"{self.base_url}local/components/form/saratov.zadolzhennost/ajax.php", data=data)
        if response.status_code == 200:
            in_list = response.json()['html'].split(">")
            in_list.pop(7)
            in_list.pop(3)
            in_list.pop(0)
            out_list = []
            for item in in_list:
                out_list.append(item.replace(item[item.find("<"):len(item)],""))
            return f'Энергосбыт (тепло и горячая вода).\n{"".join(out_list[0:2])} {"".join(out_list[2:5])}'
