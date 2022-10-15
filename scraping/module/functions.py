import json
from fake_useragent import UserAgent
import requests


con = []
turn = {}


def __(key=None, value=None, end=None, constant=con, delpth=4, path=None, **kwargs):
    _end, list_vocany, _dict, index, path =\
        constant[turn["index"]] if constant else [0, list(), dict(), 0, path]
    _dict[key] = value if value else {i: kwargs.get(i) for i in kwargs}
    if len(_dict) == delpth:
            list_vocany.append(_dict)
            _dict = {}
            if constant:
                constant[index][2] = {}
    if len(list_vocany) == end if end and end > 0 else constant[0]:
        file_path = path
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(list_vocany, file, indent=4, ensure_ascii=False)


def __exc(url, headers, path="errors.json"):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code != 200:
            __(path=path, key="errors", end=1, delpth=1, title=url, content="сайт не отвечает",
               stats_code=response.status_code)
    except Exception as exc:
        __(path=path, key="errors", end=1, delpth=1, title=url, content="сайт не отвечает")
        response = None
    return response


def get_url(func, domen, language, city="", page=0):
    user_agent = UserAgent()
    headers = {"user-agent": f"{user_agent.random}"}
    domen = domen
    city = city
    language = language
    url = f"{domen}/search/vacancy?text={language}&page={page}"
    response = __exc(url, headers)
    if response:
        func(response)
