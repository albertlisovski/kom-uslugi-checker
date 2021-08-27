import requests
from lib.provider import Provider

class Ozon(Provider):

    def check(self):
        #data = {"url": "/search/?text=%D0%BD%D1%8D%D0%BD%D0%BD%D0%B8%202&from_global=true&page_changed=true"}
        headers = {"Client-Id": "112697", "Api-Key": "9412f2cd-2e1d-4739-8e10-e03586692264"}
        response = requests.get(\
            f"{self.base_url}/product/info", headers=headers)
        if response.status_code == 200:
            return response.text
        
