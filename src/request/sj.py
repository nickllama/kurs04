import requests
import dotenv
import os
from config import URL_SJ
from src.data_json.work_with_json import WorkWithJson


dotenv.load_dotenv(".env")


class RequestsSJ(WorkWithJson):
    """Запрос на SuperJob"""

    def __init__(self, keyword, page=1) -> None:
        self.url = URL_SJ
        self.params = {"keywords": keyword, "page": page}

    def request(self) -> dict:
        """Запрос"""
        headers = {
            "X-Api-App-Id": os.getenv("SJ_API_TOKEN")
        }
        responce = requests.get(self.url, params=self.params, headers=headers)
        return WorkWithJson.save_json(responce.json()["objects"])